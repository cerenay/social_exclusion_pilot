# =============================================================================
#  power_analysis.R
#  Sample-size estimation for the new Social Exclusion 2 x 2 experiment
# -----------------------------------------------------------------------------
#  Author : Ceren Ay
#  Date   : 2026-07-13
#  Alpha  : 0.05          Power : 0.90
# -----------------------------------------------------------------------------
#
#  PURPOSE
#  -------
#  Estimate the sample size required for the primary a-priori test in the new
#  design: the Identity x Exclusion interaction on dictator-game giving.
#  Effect-size assumptions are anchored on the previous pilot study, which had
#  a different design (a single "condition" factor: chosen vs random
#  exclusion, no identity manipulation).
#
#  NEW DESIGN (target)
#  -------------------
#  Between-subjects 2 x 2 factorial:
#     Factor A  IDENTITY      : no  |  yes (minimal-group Klee / Kandinsky)
#     Factor B  EXCLUSION      : random (computer)  |  spectator (participant)
#
#  Cells map onto four of the five treatments implemented in the oTree code:
#     T1 = no identity   x random exclusion
#     T2 = no identity   x spectator exclusion
#     T4 = identity      x random exclusion
#     T5 = identity      x spectator exclusion
#  (T3 = identity x no exclusion is retained as a manipulation baseline but
#   is not part of the 2 x 2 factorial reported here.)
#
#  Outcome: EMU allocated to the recipient in the dictator game.
#  Primary test: the A x B interaction on the outcome.
#
#  PILOT (different design; used only to anchor plausible effect sizes)
#  --------------------------------------------------------------------
#  N = 381 (199 treatment, 182 control). One between-subjects factor.
#  Effect of condition (treatment vs control) on DG giving:
#      Cohen's d ~ 0.21   (small)
#      Cohen's f ~ 0.11   (small)
#  The pilot's condition factor corresponds to ONE of the new design's
#  factors (the exclusion mechanism). We therefore treat f_pilot as a
#  reasonable lower-bound estimate for the interaction in the new design.
# =============================================================================


# ---- 0. Packages ------------------------------------------------------------
# Set a CRAN mirror explicitly. When run non-interactively (Rscript, Quarto)
# R cannot prompt for a mirror, so install.packages() errors out with
# "trying to use CRAN without setting a mirror" unless one is set.
options(repos = c(CRAN = "https://cloud.r-project.org"))

required <- c("pwr", "readr", "dplyr", "tidyr", "ggplot2")
new <- setdiff(required, rownames(installed.packages()))
if (length(new) > 0) install.packages(new)
invisible(lapply(required, library, character.only = TRUE))


# ---- 1. Paths ---------------------------------------------------------------
# The pilot data folder path contains spaces; wrap in quotes when referencing.
PILOT_DIR <- "/Users/cerenay/social_exclusion_pilot/processed data and analyses"

pilot_treatment <- read_csv2(file.path(PILOT_DIR, "treatment_pilot.csv"))
pilot_control   <- read_csv2(file.path(PILOT_DIR, "control_pilot.csv"))


# ---- 2. Reproduce pilot effect sizes ---------------------------------------
# The pilot's DG amount sent is stored in `group_sent` when the participant
# was the dictator (role_dg == 1) and in `send_proxy` otherwise (strategy-
# method proxy). Reconstruct a single `dg` variable.
pilot <- bind_rows(pilot_treatment, pilot_control) %>%
  mutate(
    dg   = if_else(role_dg == 1, group_sent, send_proxy),
    fair = case_when(
      payoff_beneficiary == 10 ~ "fair",
      payoff_beneficiary  > 10 ~ "excluder",
      payoff_beneficiary  < 10 ~ "excluded"
    )
  ) %>%
  filter(!is.na(dg))

cat("\n---- Pilot marginal means (dg amount sent) ----\n")
pilot %>%
  group_by(condition) %>%
  summarise(n = n(), mean = round(mean(dg), 3), sd = round(sd(dg), 3)) %>%
  print()

cat("\n---- Pilot cell means (condition x fair status) ----\n")
pilot %>%
  group_by(condition, fair) %>%
  summarise(n = n(), mean = round(mean(dg), 3),
            sd = round(sd(dg), 3), .groups = "drop") %>%
  print()

# Cohen's d for the marginal condition effect (Welch-adjusted denominator).
d_condition <- with(pilot, {
  tv <- dg[condition == "treatment"]
  cv <- dg[condition == "control"]
  n1 <- length(tv); n2 <- length(cv)
  m1 <- mean(tv);   m2 <- mean(cv)
  s1 <- sd(tv);     s2 <- sd(cv)
  ps <- sqrt(((n1 - 1) * s1^2 + (n2 - 1) * s2^2) / (n1 + n2 - 2))
  (m1 - m2) / ps
})

# One-way ANOVA -> eta^2 -> Cohen's f
aov_cond   <- aov(dg ~ condition, data = pilot)
ss         <- summary(aov_cond)[[1]][, "Sum Sq"]
eta2_cond  <- ss[1] / sum(ss)
f_cond     <- sqrt(eta2_cond / (1 - eta2_cond))

cat(sprintf("\n---- Pilot effect sizes for condition on DG amount ----\n"))
cat(sprintf("  Cohen's d = %.3f   |d| = %.3f\n", d_condition, abs(d_condition)))
cat(sprintf("  eta^2     = %.4f\n", eta2_cond))
cat(sprintf("  Cohen's f = %.4f   [small = 0.10, medium = 0.25, large = 0.40]\n",
            f_cond))


# ---- 3. Primary power analysis ---------------------------------------------
# Target test:  Identity (A) x Exclusion (B) interaction in a 2 x 2 between-
# subjects ANOVA on DG amount sent.
#
#  df for the interaction test:
#     numerator   u = (a - 1)(b - 1)  =  1
#     denominator v = N - a * b        =  N - 4
#
#  pwr.f2.test() returns v given u, f2, alpha, power.  Total N = v + 4.
#  Cell size n = N / 4.
#
# We sweep across four effect-size scenarios so the researcher can see how
# sample-size demand scales with assumed effect size.

alpha <- 0.05
power <- 0.90

power_2x2_interaction <- function(f, alpha = 0.05, power = 0.90,
                                  a_levels = 2, b_levels = 2) {
  u   <- (a_levels - 1) * (b_levels - 1)                 # 1 for a 2 x 2
  res <- pwr.f2.test(u = u, f2 = f^2,
                     sig.level = alpha, power = power)
  N_total <- ceiling(res$v + a_levels * b_levels)        # v + 4
  data.frame(
    f            = f,
    f_squared    = round(f^2, 5),
    u_num_df     = u,
    v_denom_df   = ceiling(res$v),
    N_total      = N_total,
    n_per_cell   = ceiling(N_total / (a_levels * b_levels))
  )
}

scenarios <- data.frame(
  label = c("Pilot-derived (single-factor)",
            "Small  (Cohen benchmark)",
            "Small-to-medium",
            "Medium (Cohen benchmark)"),
  f     = c(round(f_cond, 3), 0.10, 0.15, 0.25)
)

primary_results <- do.call(rbind, lapply(seq_len(nrow(scenarios)), function(i) {
  cbind(scenario = scenarios$label[i],
        power_2x2_interaction(scenarios$f[i], alpha, power))
}))

cat(sprintf(
  "\n---- Primary a-priori power table  (alpha = %.2f, power = %.2f) ----\n",
  alpha, power))
cat("Target: Identity x Exclusion interaction (2 x 2 between-subjects ANOVA)\n\n")
print(primary_results, row.names = FALSE)


# ---- 4. Supporting analyses (secondary) ------------------------------------
# Reported here so the primary decision is not the only anchor.

## 4a. Main effect of a single factor (identity OR exclusion) in the 2 x 2.
##     Numerator df = 1, same as the interaction; expected sample sizes match
##     what pwr.f2.test yields for the same f, so the interaction table above
##     is also the main-effect table.

## 4b. Omnibus 5-treatment one-way ANOVA (T1..T5) as a robustness check.
cat("\n---- Secondary: omnibus 5-treatment one-way ANOVA ----\n")
five_treatment <- data.frame(
  f        = c(round(f_cond, 3), 0.10, 0.15, 0.25),
  scenario = c("Pilot-derived", "Small", "Small-to-medium", "Medium")
)
five_treatment$n_per_cell <- sapply(five_treatment$f, function(f) {
  ceiling(pwr.anova.test(k = 5, f = f,
                         sig.level = alpha, power = power)$n)
})
five_treatment$N_total <- five_treatment$n_per_cell * 5
print(five_treatment[, c("scenario", "f", "n_per_cell", "N_total")],
      row.names = FALSE)

## 4c. Within-subjects paired contrast (in-group vs out-group in Round 2, or
##     easy-recipient vs hard-recipient in Round 3). Every participant supplies
##     two paired observations under the strategy method.
cat("\n---- Secondary: within-subjects paired contrast ----\n")
cat("(Round 2 in-group vs out-group, OR Round 3 easy vs hard recipient)\n")
paired_scenarios <- data.frame(
  scenario = c("Small  (d = 0.20)", "Small-to-medium (d = 0.30)",
               "Medium (d = 0.50)"),
  d        = c(0.20, 0.30, 0.50)
)
paired_scenarios$n_needed <- sapply(paired_scenarios$d, function(d) {
  ceiling(pwr.t.test(d = d, sig.level = alpha, power = power,
                     type = "paired", alternative = "two.sided")$n)
})
print(paired_scenarios, row.names = FALSE)


# ---- 5. Simulation-based power analysis (Monte Carlo) ----------------------
# For each candidate cell size and each assumed effect size, generate
# n_sims replicate datasets under the specified 2 x 2 interaction pattern,
# fit an ANOVA, and count how often the interaction reaches p < alpha.
#
# The cell means are chosen so that Cohen's f of the pure interaction
# equals the target value:
#
#     Cell (A1, B1) = -delta          Cell (A1, B2) = +delta
#     Cell (A2, B1) = +delta          Cell (A2, B2) = -delta
#
# with delta = f * SD.  This is a "crossover" pattern with no main effects,
# giving a clean interaction test.  Within-cell variance is Normal with
# SD anchored to the pilot's DG-amount SD, so the simulated noise level is
# realistic for the outcome you'll actually observe.

DESIGN_DIR <- "/Users/cerenay/social_exclusion_pilot/2025_new_design_and_experiment/Design"

# Within-cell SD anchor: use the pilot's overall SD of the DG amount sent.
pilot_sd <- sd(pilot$dg)
cat(sprintf("\nSimulation SD anchor (pilot DG amount): %.3f\n", pilot_sd))

simulate_power_2x2 <- function(n_per_cell,
                               f,
                               sd     = pilot_sd,
                               n_sims = 500,
                               alpha  = 0.05) {
  delta <- f * sd
  cell_means <- c(-delta, +delta, +delta, -delta)  # A1B1, A1B2, A2B1, A2B2
  # Build the fixed design vectors once
  A <- factor(rep(c("A1", "A1", "A2", "A2"), each = n_per_cell))
  B <- factor(rep(c("B1", "B2", "B1", "B2"), each = n_per_cell))
  mu <- rep(cell_means, each = n_per_cell)
  n_sig <- 0L
  for (i in seq_len(n_sims)) {
    y   <- mu + rnorm(length(mu), sd = sd)
    fit <- aov(y ~ A * B)
    p   <- summary(fit)[[1]]["A:B", "Pr(>F)"]
    if (!is.na(p) && p < alpha) n_sig <- n_sig + 1L
  }
  n_sig / n_sims
}

# Grid: sample sizes per cell x effect sizes.  Add or remove points as you
# wish; runtime scales linearly with n_grid * f_grid * n_sims_per_point.
n_grid           <- c(20, 40, 60, 80, 100, 120, 150, 200, 250)
f_grid           <- c(0.10, 0.15, 0.20, 0.25)
n_sims_per_point <- 500

cat(sprintf("\nSimulating: %d cell sizes x %d effect sizes x %d sims each = %d fits.\n",
            length(n_grid), length(f_grid), n_sims_per_point,
            length(n_grid) * length(f_grid) * n_sims_per_point))
cat("This typically takes 1-3 minutes on a laptop; reduce n_sims_per_point\n")
cat("to run faster (at the cost of noisier power estimates).\n")

set.seed(2026)
sim_grid <- expand.grid(n_per_cell = n_grid, f = f_grid,
                        KEEP.OUT.ATTRS = FALSE)
sim_grid$power <- mapply(
  simulate_power_2x2,
  n_per_cell = sim_grid$n_per_cell,
  f          = sim_grid$f,
  MoreArgs   = list(sd = pilot_sd, n_sims = n_sims_per_point, alpha = alpha)
)
sim_grid$N_total <- sim_grid$n_per_cell * 4

cat("\n---- Simulated power table (rows = cell size, cols = Cohen's f) ----\n")
sim_wide <- pivot_wider(sim_grid[, c("n_per_cell", "f", "power")],
                        names_from = f, values_from = power,
                        names_prefix = "f=")
print(sim_wide, row.names = FALSE)

# For each effect size, report the smallest n_per_cell that reached >= 0.90.
target_power <- 0.90
cat(sprintf("\n---- Smallest n per cell that reached simulated power >= %.2f ----\n",
            target_power))
achieved <- sim_grid %>%
  group_by(f) %>%
  filter(power >= target_power) %>%
  summarise(n_per_cell_min = min(n_per_cell),
            N_total_min    = min(N_total),
            power_at_min   = power[which.min(n_per_cell)],
            .groups = "drop")
print(achieved, row.names = FALSE)


# ---- 6. Power curve plot ---------------------------------------------------
sim_grid$f_label <- paste0("f = ", format(sim_grid$f, nsmall = 2))

plot_power <- ggplot(sim_grid,
                     aes(x = n_per_cell, y = power,
                         color = f_label, group = f_label)) +
  geom_hline(yintercept = c(0.80, 0.90),
             linetype = "dashed", color = "grey55") +
  annotate("text", x = min(n_grid), y = 0.80, label = "power = 0.80",
           vjust = -0.4, hjust = 0, size = 3.2, color = "grey45") +
  annotate("text", x = min(n_grid), y = 0.90, label = "power = 0.90",
           vjust = -0.4, hjust = 0, size = 3.2, color = "grey45") +
  geom_line(size = 1) +
  geom_point(size = 2.5) +
  scale_y_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.1)) +
  scale_x_continuous(breaks = n_grid) +
  labs(
    title    = "Simulated power curves for the 2 x 2 interaction",
    subtitle = sprintf(
      "Within-cell SD = %.2f (pilot anchor), alpha = %.2f, %d simulations per point",
      pilot_sd, alpha, n_sims_per_point),
    x        = "Sample size per cell",
    y        = "Simulated power",
    color    = "Effect size"
  ) +
  theme_minimal(base_size = 12) +
  theme(legend.position = "right",
        panel.grid.minor = element_blank())

print(plot_power)

plot_path <- file.path(DESIGN_DIR, "power_curves.png")
ggsave(plot_path, plot = plot_power, width = 9, height = 6, dpi = 150)
cat(sprintf("\nPower-curve plot saved to: %s\n", plot_path))


# ---- 7. Alternative anchor: Chen & Li (2009) -------------------------------
# The pilot manipulated only the exclusion mechanism (chosen vs random) and
# is therefore a lower bound on the interaction of interest. An alternative
# reference point is Chen, Y., & Li, S. X. (2009). "Group Identity and
# Social Preferences." American Economic Review, 99(1), 431-457 — the
# canonical paper that introduced the Klee/Kandinsky minimal-group paradigm
# and reported ingroup/outgroup differences in dictator giving.
#
# Key statistics reported in Chen & Li (2009):
#   * Other-other allocation task: the ingroup-vs-outgroup allocation
#     difference (normalised by endowment) ranges from 32.2% to 38.4%
#     across the five rounds, significant at the 1% level for each round
#     (Section II results; N = 566 subjects total).
#   * Identity parameter for charity a = 0.467 (95% CI approximately
#     [0.247, 0.687]) — participants give 47% more weight to another
#     participant's payoff when that participant is an ingroup match
#     (Table 2, MLE; N = 1896 obs from 432 treatment subjects).
#   * Identity parameter for envy b = -0.931 — envy is 93% lower toward
#     ingroup than toward outgroup matches (Table 2).
#   * In dictator-game choices (Appendix A, Dict 1-5), player A ingroup
#     vs outgroup choice proportions differ by ~0.12; player B by ~0.15.
#
# Converting these to Cohen's f for a 2 x 2 between-subjects ANOVA:
#   * Behavioural choice-proportion differences (Cohen's h = 0.24-0.32)
#     translate to Cohen's f ~ 0.12-0.16 for the identity main effect.
#   * The utility-parameter interpretation (47% charity increase, with a
#     35% mean allocation gap) translates to Cohen's f ~ 0.20-0.30.
#
# Because these are Chen & Li's *identity main effect* (not an interaction
# with a second between-subjects factor), the corresponding INTERACTION
# effect in the new 2 x 2 could plausibly be smaller, equal, or larger.
# We report the range so the researcher can pick the value that best
# reflects their theoretical expectation for the identity x exclusion
# interaction.

chen_li_scenarios <- data.frame(
  scenario = c("Chen & Li (behavioural, low)",
               "Chen & Li (behavioural, mid)",
               "Chen & Li (utility param, mid)",
               "Chen & Li (utility param, high)"),
  f        = c(0.13, 0.16, 0.20, 0.25)
)

chen_li_results <- do.call(rbind, lapply(seq_len(nrow(chen_li_scenarios)), function(i) {
  cbind(scenario = chen_li_scenarios$scenario[i],
        power_2x2_interaction(chen_li_scenarios$f[i], alpha, power))
}))
chen_li_results$N_recruit <- ceiling(chen_li_results$N_total / (1 - 0.20))

cat("\n---- Chen & Li (2009) anchor: sample-size table -----\n")
cat("(alpha = 0.05, power = 0.90, 20% attrition buffer applied)\n\n")
print(chen_li_results, row.names = FALSE)


# ---- 8. Recommendation & rationale (printed) -------------------------------
cat("\n=============================================================\n")
cat("  RECOMMENDATION\n")
cat("=============================================================\n")
cat("The pilot's effect size for the exclusion-mechanism contrast was\n")
cat(sprintf("  Cohen's f = %.3f (small, on the low end of the Cohen benchmarks).\n\n", f_cond))
cat("Because the pilot manipulated only one of the new design's two factors,\n")
cat("the interaction in the new 2 x 2 could plausibly be smaller than, equal\n")
cat("to, or larger than the pilot's marginal effect. We therefore report a\n")
cat("range and recommend the researcher pick a target f based on the smallest\n")
cat("interaction of substantive interest.\n\n")

cat("If the smallest interaction of interest is:\n")
cat("  * f = 0.10 (small)          -> n per cell shown above; total N is large\n")
cat("                                  and often prohibitive online (thousands).\n")
cat("  * f = 0.15 (small-to-med)   -> a common preregistration target for\n")
cat("                                  online experiments.\n")
cat("  * f = 0.25 (medium)         -> most feasible; assumes the identity\n")
cat("                                  manipulation amplifies the exclusion\n")
cat("                                  effect meaningfully.\n\n")
cat("A defensible preregistration would (a) power for f = 0.15 as primary,\n")
cat("(b) note f = 0.25 as the smallest 'theoretically interesting' size, and\n")
cat("(c) plan a sequential design or a second wave if the observed effect is\n")
cat("smaller than f = 0.15.\n\n")

cat("Because the design also includes within-subjects paired contrasts\n")
cat("(Round 2 in-group vs out-group; Round 3 easy vs hard recipient), the\n")
cat("paired-samples table above shows that these tests are considerably\n")
cat("cheaper in sample size than the between-subjects interaction, so the\n")
cat("between-subjects interaction is the binding constraint.\n")

cat("\nCross-check: the analytical table (section 3) and the simulation table\n")
cat("(section 5) should agree closely at the target power; any large mismatch\n")
cat("would indicate a violated assumption (non-normal errors, unequal SDs,\n")
cat("etc.).  Inspect power_curves.png for the full sample-size / effect-size\n")
cat("trade-off surface.\n")

# ---- 9. Attrition / exclusion buffer ---------------------------------------
# Online samples typically lose 10-25% to attention checks, dropouts, or
# comprehension failures. Inflate the target N accordingly.
buffer_rate <- 0.20     # 20% attrition buffer
cat(sprintf(
  "\nApplying a %d%% attrition / exclusion buffer to the primary table:\n",
  round(100 * buffer_rate)))
primary_results$N_recruit <- ceiling(primary_results$N_total / (1 - buffer_rate))
print(primary_results[, c("scenario", "f", "N_total", "N_recruit")],
      row.names = FALSE)

# =============================================================================
#  End of power_analysis.R
# =============================================================================
