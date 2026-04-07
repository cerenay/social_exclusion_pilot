#!/usr/bin/env python3
"""
generate_preview.py
===================
Run this script from the social_exclusion_26 folder to regenerate
the full-experiment HTML preview file:

    python generate_preview.py

The script reads the CSS theme directly from:
    social_exc_2025/_templates/global/Page.html

and writes the preview to:
    screenshots/experiment_preview.html

That way, any changes you make to the theme are automatically reflected
in the preview the next time you run this script.
"""

import os
import re
from datetime import date

# ── Paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR   = os.path.dirname(os.path.abspath(__file__))
PAGE_HTML    = os.path.join(SCRIPT_DIR, "social_exc_2025", "_templates", "global", "Page.html")
OUTPUT_DIR   = os.path.join(SCRIPT_DIR, "screenshots")
OUTPUT_FILE  = os.path.join(OUTPUT_DIR, "experiment_preview.html")


# ── Extract CSS from Page.html ─────────────────────────────────────────────────
def extract_css(page_html_path: str) -> str:
    """Pull the contents of the <style> block from Page.html."""
    with open(page_html_path, encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"<style>(.*?)</style>", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    raise ValueError(f"Could not find <style> block in {page_html_path}")


# ── Screen definitions ─────────────────────────────────────────────────────────
# Each screen is a dict with:
#   label   – shown above the page shell
#   title   – the page <h2> title
#   body    – HTML content inside .content-card

SCREENS = [

    # ── painting_choice ────────────────────────────────────────────────────────
    {
        "app": "painting_choice",
        "label": "Screen 1 · Welcome & Consent",
        "title": "Welcome!",
        "body": """
<p>Thank you for participating in this study on decision-making.</p>
<p>During this study, you will earn money. How much you earn depends on your decisions,
the decisions of other participants, and an element of chance.</p>
<p>We will speak in terms of Experimental Monetary Units (EMU) instead of Pounds.
Your payoffs will be calculated in terms of EMU and then converted to Pounds at the end of
the study, at a rate of 100 EMU = X Pound.</p>
<p>The study is divided into 3 parts, and your total earnings will be the sum of your
payoffs in each part. At the end of the study, we will ask you to complete a short survey.</p>
<p>We appreciate you taking the time to participate in this study.
If you have any questions or comments, please contact: XXX.</p>
<div style="margin-top:20px;">
  <label style="font-weight:600;">Do you consent to participate?</label><br><br>
  <label style="margin-right:20px;"><input type="radio" name="consent" value="accept"> Accept</label>
  <label><input type="radio" name="consent" value="decline"> Decline</label>
</div>
<div style="margin-top:16px; padding:12px 16px; background:#f8f9fa;
     border-left:3px solid #6c757d; border-radius:6px; display:none;">
  <p style="margin:0;">You have selected not to proceed with this study.
  We appreciate your consideration!</p>
</div>
"""
    },
    {
        "app": "painting_choice",
        "label": "Screen 2 · Part 1 Introduction",
        "title": "Part 1",
        "body": """
<p>In Part 1 everyone will be shown 5 pairs of paintings by two artists.
You will be asked to choose which painting in each pair you prefer.
You will then be classified into one of two groups, based on which artist you prefer.</p>
<p>After Part 1 is complete, we will provide instructions for the next parts
of the experiment.</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "painting_choice",
        "label": "Screen 3 · Painting Preferences",
        "title": "Painting Preferences",
        "body": """
<p>Now, please choose which painting you prefer by clicking on either A or B from each pair.
After everyone submits answers, you will be privately informed of which group you are in.</p>
<p>Note that there are no right or wrong answers.
Please base your choices solely on your own preferences.</p>
<div style="margin-bottom:24px;">
  <p><strong>Pair 1</strong></p>
  <div style="display:flex; justify-content:space-around; align-items:center; gap:20px;">
    <div style="text-align:center;">
      <div style="width:210px; height:150px; background:#E4E4E7; border-radius:8px;
           display:flex; align-items:center; justify-content:center;
           color:var(--text-muted); font-size:0.85rem; margin-bottom:8px;">Painting A</div>
      <label><input type="radio" name="pair1" value="A"> A</label>
    </div>
    <div style="text-align:center;">
      <div style="width:210px; height:150px; background:#E4E4E7; border-radius:8px;
           display:flex; align-items:center; justify-content:center;
           color:var(--text-muted); font-size:0.85rem; margin-bottom:8px;">Painting B</div>
      <label><input type="radio" name="pair1" value="B"> B</label>
    </div>
  </div>
</div>
<p style="color:var(--text-muted); font-size:0.85rem;">⋯ Pairs 2–5 follow the same layout ⋯</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "painting_choice",
        "label": "Screen 4 · Group Assignment (Klee example)",
        "title": "Your Painting Group",
        "body": """
<p>Based on your choices, you prefer the paintings by
<span class="tag-klee">Klee</span>.</p>
<p>You are assigned to the <span class="tag-klee">Klee</span> group.</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "painting_choice",
        "label": "Screen 5 · Reasons for Choice",
        "title": "Reasons for choice",
        "body": """
<p>Why did you prefer these paintings?
<em>You may select more than one option.</em></p>
<div style="margin-bottom:20px;">
  <div style="margin-bottom:10px;"><label><input type="checkbox"> The use of colour</label></div>
  <div style="margin-bottom:10px;"><label><input type="checkbox"> The composition</label></div>
  <div style="margin-bottom:10px;"><label><input type="checkbox"> The style</label></div>
  <div style="margin-bottom:10px;"><label><input type="checkbox"> The subject matter</label></div>
  <div style="margin-bottom:10px;"><label><input type="checkbox"> The emotional expression</label></div>
  <div style="margin-bottom:10px;">
    <label><input type="checkbox"> Other</label><br>
    <input type="text" placeholder="Please specify..."
           style="display:none; margin-top:5px; width:300px;">
  </div>
</div>
<span class="btn-primary">Next →</span>
"""
    },

    # ── counting_matrix ────────────────────────────────────────────────────────
    {
        "app": "counting_matrix",
        "label": "Screen 6 · Part 2 Instructions (T5 example – identity + spectator exclusion)",
        "title": "Part 2",
        "body": """
<p>Now we start Part 2 of the study.</p>
<p>You will be asked to perform a task that involves moving a slider to a position
corresponding to a displayed range of numbers indicated.</p>
<p>You will see a screen with 5 sliders: each slider is initially positioned at 0 and can
be moved as far as 100. When you move the slider, you will see a number showing its current
position. Your task is to position each slider at a number within the indicated range.</p>
<p>There are two versions of this task: an <em>easy</em> task and a <em>hard</em> task.
The two versions differ only in the size of the number range you need to match on the slider.</p>
<p>Another participant, who may or may not belong to your
<span class="tag-kandinsky">Kandinsky</span> or <span class="tag-klee">Klee</span> group,
will also complete the task.
<strong>One of you will be assigned the easy task and the other one will be assigned the
hard task.</strong> The tasks are assigned by an <strong>independent participant</strong>,
who may or may not belong to your
<span class="tag-kandinsky">Kandinsky</span> or <span class="tag-klee">Klee</span> group.
The only information this independent participant has is the painting group of each
participant.</p>
<p>You will receive additional EMUs for completing the task.
Both participants must complete the tasks to continue to Part 3.</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "counting_matrix",
        "label": "Screen 7 · Slider Practice Round",
        "title": "Slider Task Practice Round",
        "body": """
<p>This is a practice round for the slider task before completing the actual task.</p>
<p>In this round you can move the slider as many times as you need to become familiar
with it. Note that in the actual task, you can only move each slider once.</p>
<p>Please position the slider in the range: <strong>40–60</strong>.</p>
<div style="margin-bottom:25px;">
  <label>Practice slider</label><br>
  <input type="range" min="0" max="100" value="48" style="width:400px;">
  <span class="slider-value">48</span>
</div>
<p>Recall that the two versions of the task (easy/hard) differ in the size of the
number range you need to position the slider.</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "counting_matrix",
        "label": "Screen 8 · Slider Task (Easy version)",
        "title": "Slider Task",
        "body": """
<p>You have been assigned to the <strong>easy</strong> version of the slider task.</p>
<p>Please use the sliders below to indicate your answers.
Once you move a slider, your choice will be recorded and cannot be changed.</p>
<p>Each slider has its own valid range, shown below it.</p>
<div style="margin-bottom:30px;">
  <label><strong>Slider 1</strong></label><br>
  <input type="range" min="0" max="100" value="12" style="width:400px;">
  <span class="slider-value">12</span><br>
  <small>Valid range: 0–20</small>
</div>
<div style="margin-bottom:30px;">
  <label><strong>Slider 2</strong></label><br>
  <input type="range" min="0" max="100" value="0" style="width:400px;">
  <span class="slider-value"></span><br>
  <small>Valid range: 20–40</small>
</div>
<p style="color:var(--text-muted); font-size:0.85rem;">⋯ Sliders 3–5 follow the same layout ⋯</p>
<span class="btn-disabled">Next →</span>
<span style="margin-left:10px; color:var(--text-muted); font-size:0.9em;">
  Please move all 5 sliders before continuing.</span>
"""
    },
    {
        "app": "counting_matrix",
        "label": "Screen 9 · Slider Task Results",
        "title": "Your Results",
        "body": """
<p>You have now completed the slider task. Your results are shown below.</p>
<table class="likert-table" style="margin-bottom:20px;">
  <thead>
    <tr>
      <th style="text-align:left; min-width:80px;">Slider</th>
      <th>Your answer</th>
      <th>Valid range</th>
      <th>Correct?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:left;">1</td><td>12</td><td>0–20</td>
        <td><span style="color:var(--green); font-weight:600;">✓</span></td></tr>
    <tr><td style="text-align:left;">2</td><td>35</td><td>20–40</td>
        <td><span style="color:var(--green); font-weight:600;">✓</span></td></tr>
    <tr><td style="text-align:left;">3</td><td>55</td><td>40–60</td>
        <td><span style="color:var(--green); font-weight:600;">✓</span></td></tr>
    <tr><td style="text-align:left;">4</td><td>72</td><td>60–80</td>
        <td><span style="color:var(--green); font-weight:600;">✓</span></td></tr>
    <tr><td style="text-align:left;">5</td><td>95</td><td>80–100</td>
        <td><span style="color:var(--green); font-weight:600;">✓</span></td></tr>
  </tbody>
</table>
<p><strong>Number of correct answers: 5 out of 5</strong></p>
<p>For completing Part 2 of the study, participants receive <strong>X EMUs</strong>.</p>
<p>All participants who complete Part 2 receive the same amount.
The amount earned in this part does not depend on which version of the slider task
you were assigned to.</p>
<span class="btn-primary">Next →</span>
"""
    },

    # ── dictator ───────────────────────────────────────────────────────────────
    {
        "app": "dictator",
        "label": "Screen 10 · Part 3 Introduction",
        "title": "Part 3",
        "body": """
<p>Now we start Part 3. You will be randomly and anonymously paired with a
<strong>new participant</strong>.</p>
<p>The independent participant who assigned the tasks in Part 2 will not participate in
this part of the study.</p>
<p>You will be asked to make decisions in 3 rounds. In each round, you will have a certain
number of EMU. You will be asked to allocate these EMUs between yourself and the other
participant.</p>
<p>Each round presents a different decision situation, which we call scenarios.</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "dictator",
        "label": "Screen 11 · Round 1 – Baseline Allocation",
        "title": "Round 1",
        "body": """
<p>Please indicate how many EMU you keep for yourself and how many you allocate to the
other participant <em>under the scenario below</em>.</p>
<p>You have <strong>20 EMU</strong> to allocate.</p>
<div style="margin-bottom:15px;">
  <label><strong>You (EMU)</strong></label><br>
  <input type="number" min="0" max="20" value="10" style="width:100px;">
</div>
<div style="margin-bottom:15px;">
  <label><strong>Other participant (EMU)</strong></label><br>
  <input type="number" min="0" max="20" value="10" style="width:100px;">
</div>
<div class="sum-box">Total: <strong>20 / 20 EMU</strong></div>
<br>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "dictator",
        "label": "Screen 12 · Round 2 – Group-Identity Scenarios",
        "title": "Round 2",
        "body": """
<p>Please indicate how many EMU you keep for yourself and how many you allocate to the
other participant <em>under the two scenarios below</em>.</p>
<p>You have <strong>20 EMU</strong> to allocate in each scenario.</p>
<div class="section-block">
  <div class="section-title">Scenario 1</div>
  <p>The other participant is from your painting group
     (<span class="tag-klee">Klee</span>)</p>
  <div style="margin-bottom:15px;">
    <label><strong>You (EMU)</strong></label><br>
    <input type="number" min="0" max="20" value="10" style="width:100px;">
  </div>
  <div style="margin-bottom:15px;">
    <label><strong>Other participant (EMU)</strong></label><br>
    <input type="number" min="0" max="20" value="10" style="width:100px;">
  </div>
  <div class="sum-box">Total: <strong>20 / 20 EMU</strong></div>
</div>
<div class="section-block">
  <div class="section-title">Scenario 2</div>
  <p>The other participant is from the other painting group
     (<span class="tag-kandinsky">Kandinsky</span>)</p>
  <div style="margin-bottom:15px;">
    <label><strong>You (EMU)</strong></label><br>
    <input type="number" min="0" max="20" value="10" style="width:100px;">
  </div>
  <div style="margin-bottom:15px;">
    <label><strong>Other participant (EMU)</strong></label><br>
    <input type="number" min="0" max="20" value="10" style="width:100px;">
  </div>
  <div class="sum-box">Total: <strong>20 / 20 EMU</strong></div>
</div>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "dictator",
        "label": "Screen 13 · Round 3 – Task-Difficulty Scenarios",
        "title": "Round 3",
        "body": """
<p>Please indicate how many EMU you keep for yourself and how many you allocate to the
other participant <em>under the two scenarios below</em>.</p>
<p>You have <strong>20 EMU</strong> to allocate in each scenario.</p>
<div class="section-block">
  <div class="section-title">Scenario 1</div>
  <p>The other participant previously completed the <em>easy</em> slider task.</p>
  <div style="margin-bottom:15px;">
    <label><strong>You (EMU)</strong></label><br>
    <input type="number" min="0" max="20" value="10" style="width:100px;">
  </div>
  <div style="margin-bottom:15px;">
    <label><strong>Other participant (EMU)</strong></label><br>
    <input type="number" min="0" max="20" value="10" style="width:100px;">
  </div>
  <div class="sum-box">Total: <strong>20 / 20 EMU</strong></div>
</div>
<div class="section-block">
  <div class="section-title">Scenario 2</div>
  <p>The other participant previously completed the <em>hard</em> slider task.</p>
  <div style="margin-bottom:15px;">
    <label><strong>You (EMU)</strong></label><br>
    <input type="number" min="0" max="20" value="10" style="width:100px;">
  </div>
  <div style="margin-bottom:15px;">
    <label><strong>Other participant (EMU)</strong></label><br>
    <input type="number" min="0" max="20" value="10" style="width:100px;">
  </div>
  <div class="sum-box">Total: <strong>20 / 20 EMU</strong></div>
</div>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "dictator",
        "label": "Screen 14 · Part 3 Results",
        "title": "Your Results",
        "body": """
<p>In Part 3, round X and scenario (1 or 2) were randomly selected to compute the payoffs.</p>
<p>Selected round: <strong>Round 2</strong></p>
<p>You decided to send: <strong>10</strong> EMUs</p>
<p>You kept: <strong>10</strong> EMUs</p>
<p>Your payoff from Part 3 is <strong>10</strong> EMUs</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "dictator",
        "label": "Screen 15 · Total Payoffs & Exchange Rate",
        "title": "Total payoffs and exchange rate",
        "body": """
<p>Your payoff from Part 1 is X EMUs.</p>
<p>Your payoff from Part 2 is X EMUs.</p>
<p>Your payoff from Part 3 is X EMUs.</p>
<p>Your total payoff is X EMUs.</p>
<p>The exchange rate is £1 = X EMUs.</p>
<p>So, your earnings from this experiment are £.</p>
<p>The total of your payments will be transferred to you through Prolific.</p>
<p>Now you will be asked to complete a survey.</p>
<span class="btn-primary">Next →</span>
"""
    },

    # ── postExp_survey ─────────────────────────────────────────────────────────
    {
        "app": "postExp_survey",
        "label": "Screen 16 · Survey – Familiarity with Artists",
        "title": "Final survey",
        "body": """
<p>Please answer the following survey questions. Your answers will be used for this study
only. Individual data will not be exposed.</p>
<div style="margin-bottom:20px;">
  <label><strong>Question 1 (e.g. how many experiments have you taken part in?)</strong></label><br>
  <select style="width:200px; margin-top:6px;">
    <option>0</option><option>1–3</option><option>4–10</option><option>11+</option>
  </select>
</div>
<hr>
<p>Before this study, how familiar were you with paintings made by…?</p>
<table class="likert-table">
  <thead>
    <tr>
      <th>Artist</th>
      <th>Very unfamiliar</th><th>Unfamiliar</th><th>Neither</th>
      <th>Familiar</th><th>Very familiar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left;">Klee</td>
      <td><input type="radio" name="fam_klee" value="1"></td>
      <td><input type="radio" name="fam_klee" value="2" checked></td>
      <td><input type="radio" name="fam_klee" value="3"></td>
      <td><input type="radio" name="fam_klee" value="4"></td>
      <td><input type="radio" name="fam_klee" value="5"></td>
    </tr>
    <tr>
      <td style="text-align:left;">Kandinsky</td>
      <td><input type="radio" name="fam_kan" value="1"></td>
      <td><input type="radio" name="fam_kan" value="2"></td>
      <td><input type="radio" name="fam_kan" value="3" checked></td>
      <td><input type="radio" name="fam_kan" value="4"></td>
      <td><input type="radio" name="fam_kan" value="5"></td>
    </tr>
  </tbody>
</table>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "postExp_survey",
        "label": "Screen 17 · Survey – Group & Task Feelings (Agree/Disagree)",
        "title": "Questions about the Group and the Slider Task",
        "body": """
<p>Please indicate how you feel right now about your group and the task assignment
you just received.</p>
<table class="likert-table">
  <thead>
    <tr>
      <th>Statement</th>
      <th>Strongly disagree</th><th>Disagree</th><th>Neither</th>
      <th>Agree</th><th>Strongly agree</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left;">I feel proud to be a member of the Klee group.</td>
      <td><input type="radio" name="q3" value="1"></td>
      <td><input type="radio" name="q3" value="2"></td>
      <td><input type="radio" name="q3" value="3" checked></td>
      <td><input type="radio" name="q3" value="4"></td>
      <td><input type="radio" name="q3" value="5"></td>
    </tr>
    <tr>
      <td style="text-align:left;">I feel that the task assignment was fair.</td>
      <td><input type="radio" name="q4" value="1"></td>
      <td><input type="radio" name="q4" value="2" checked></td>
      <td><input type="radio" name="q4" value="3"></td>
      <td><input type="radio" name="q4" value="4"></td>
      <td><input type="radio" name="q4" value="5"></td>
    </tr>
    <tr>
      <td style="text-align:left; color:var(--text-muted); font-size:0.85rem;" colspan="6">
        ⋯ Questions 3–10 follow the same pattern ⋯</td>
    </tr>
  </tbody>
</table>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "postExp_survey",
        "label": "Screen 18 · Survey – Emotions (Extent)",
        "title": "Questions about the Group and the Slider Task",
        "body": """
<p>Right now, to what extent do you feel each emotion?</p>
<table class="likert-table">
  <thead>
    <tr>
      <th>Emotion</th>
      <th>Not at all</th><th>To some extent</th><th>Moderately</th>
      <th>Very much</th><th>Extremely</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left;">Upset</td>
      <td><input type="radio" name="q_upset" value="1" checked></td>
      <td><input type="radio" name="q_upset" value="2"></td>
      <td><input type="radio" name="q_upset" value="3"></td>
      <td><input type="radio" name="q_upset" value="4"></td>
      <td><input type="radio" name="q_upset" value="5"></td>
    </tr>
    <tr>
      <td style="text-align:left;">Angry</td>
      <td><input type="radio" name="q_angry" value="1" checked></td>
      <td><input type="radio" name="q_angry" value="2"></td>
      <td><input type="radio" name="q_angry" value="3"></td>
      <td><input type="radio" name="q_angry" value="4"></td>
      <td><input type="radio" name="q_angry" value="5"></td>
    </tr>
    <tr>
      <td style="text-align:left; color:var(--text-muted); font-size:0.85rem;" colspan="6">
        ⋯ Sad, Anxious, Frustrated, Discouraged ⋯</td>
    </tr>
  </tbody>
</table>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "postExp_survey",
        "label": "Screen 19 · Survey – Questions about the Allocation Task",
        "title": "Questions about the Allocation Task",
        "body": """
<p>Please answer these questions about the allocation task you performed in Part 3
of this study.</p>
<div style="margin-bottom:20px;">
  <label><strong>Q12. What influenced your allocation decisions?</strong></label><br>
  <div style="margin-top:8px;">
    <label style="display:block; margin-bottom:6px;">
      <input type="radio" name="q12" value="1"> The other person's painting group</label>
    <label style="display:block; margin-bottom:6px;">
      <input type="radio" name="q12" value="2"> The other person's task difficulty</label>
    <label style="display:block; margin-bottom:6px;">
      <input type="radio" name="q12" value="3"> I tried to be fair</label>
    <label style="display:block; margin-bottom:6px;">
      <input type="radio" name="q12" value="other"> Other - Please specify:</label>
    <input type="text" placeholder="Please specify..."
           style="display:none; width:350px; padding:4px 8px;">
  </div>
</div>
<p style="color:var(--text-muted); font-size:0.85rem;">
  ⋯ Questions 13–16b follow the same layout ⋯</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "postExp_survey",
        "label": "Screen 20 · Survey – Demographics",
        "title": "Some Questions About You",
        "body": """
<div style="margin-bottom:20px;">
  <label><strong>Age</strong></label><br>
  <input type="number" style="width:100px; margin-top:6px;" value="28">
</div>
<div style="margin-bottom:20px;">
  <label><strong>Gender</strong></label><br>
  <div style="margin-top:8px;">
    <label style="margin-right:16px;"><input type="radio" name="gender" value="M"> Male</label>
    <label style="margin-right:16px;">
      <input type="radio" name="gender" value="F" checked> Female</label>
    <label><input type="radio" name="gender" value="O"> Other</label>
  </div>
</div>
<div style="margin-bottom:20px;">
  <label><strong>Have you studied economics?</strong></label><br>
  <div style="margin-top:8px;">
    <label style="margin-right:16px;">
      <input type="radio" name="econ" value="Yes"> Yes</label>
    <label><input type="radio" name="econ" value="No" checked> No</label>
  </div>
</div>
<p style="color:var(--text-muted); font-size:0.85rem;">
  ⋯ Background, donation questions follow ⋯</p>
<span class="btn-primary">Next →</span>
"""
    },
    {
        "app": "postExp_survey",
        "label": "Screen 21 · Thank You",
        "title": "Thank you!",
        "body": """
<p>Thank you for your participation in our study. Please click the blue arrow button to
continue to the completion page of the survey, you will be redirected to a new page.</p>
<span class="btn-primary">Next →</span>
"""
    },
]


# ── HTML builder ───────────────────────────────────────────────────────────────
def build_screen(screen: dict) -> str:
    return f"""
<div class="screen-label">{screen['label']}</div>
<div class="page-shell">
  <h2 class="page-title">{screen['title']}</h2>
  <div class="page-body">
    <div class="content-card">
{screen['body']}
    </div>
  </div>
</div>
"""


def build_app_divider(app_name: str) -> str:
    return f"""
<div class="app-divider">
  <hr><span>{app_name}</span><hr>
</div>
"""


def build_html(css: str, screens: list) -> str:
    # Group screens by app and insert dividers
    sections = []
    current_app = None
    for screen in screens:
        if screen["app"] != current_app:
            current_app = screen["app"]
            sections.append(build_app_divider(current_app))
        sections.append(build_screen(screen))

    body_content = "\n".join(sections)
    today = date.today().strftime("%B %Y")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Social Exclusion Experiment – Full Preview</title>
<style>
/* ── Theme CSS (auto-extracted from _templates/global/Page.html) ── */
{css}

/* ── Preview shell styles ── */
*, *::before, *::after {{ box-sizing: border-box; }}
body {{
  background: #E8E8EC;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  margin: 0;
  padding: 40px 20px;
}}
.screen-label {{
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #6366F1;
  margin: 48px auto 6px;
  max-width: 760px;
}}
.screen-label:first-of-type {{ margin-top: 0; }}
.page-shell {{
  max-width: 760px;
  margin: 0 auto 8px;
  background: var(--bg);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0,0,0,0.12);
}}
.page-title {{
  font-size: 1.45rem !important;
  font-weight: 600 !important;
  color: var(--text-main) !important;
  text-align: center !important;
  padding: 30px 36px 22px !important;
  margin: 0 !important;
  border-bottom: 1px solid var(--border) !important;
  background: var(--card-bg) !important;
  letter-spacing: -0.01em !important;
}}
.page-body {{
  padding: 28px 36px 32px;
  background: var(--bg);
}}
.btn-primary {{
  background: var(--accent);
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 10px 28px;
  font-size: 0.95rem;
  font-weight: 500;
  color: #fff;
  cursor: pointer;
  margin-top: 24px;
  display: inline-block;
}}
.btn-disabled {{
  background: #A1A1AA;
  border: 1px solid #A1A1AA;
  border-radius: 8px;
  padding: 10px 28px;
  font-size: 0.95rem;
  font-weight: 500;
  color: #fff;
  cursor: not-allowed;
  margin-top: 24px;
  display: inline-block;
}}
.app-divider {{
  max-width: 760px;
  margin: 56px auto 12px;
  display: flex;
  align-items: center;
  gap: 14px;
}}
.app-divider span {{
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #52525B;
  white-space: nowrap;
}}
.app-divider hr {{
  flex: 1;
  border: none;
  border-top: 1px solid #C4C4CC;
  margin: 0;
}}
.footer {{
  max-width: 760px;
  margin: 56px auto 0;
  text-align: center;
  font-size: 0.78rem;
  color: var(--text-muted);
  padding-bottom: 40px;
}}
</style>
</head>
<body>

{body_content}

<div class="footer">
  Social Exclusion Experiment &middot; Full Preview &middot; Generated {today}
</div>

</body>
</html>
"""


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    # 1. Extract CSS
    print(f"Reading CSS from: {PAGE_HTML}")
    try:
        css = extract_css(PAGE_HTML)
        print("  ✓ CSS extracted successfully.")
    except (FileNotFoundError, ValueError) as exc:
        print(f"  ✗ Error: {exc}")
        raise SystemExit(1)

    # 2. Build HTML
    print(f"Building preview for {len(SCREENS)} screens across "
          f"{len(set(s['app'] for s in SCREENS))} apps...")
    html = build_html(css, SCREENS)

    # 3. Write output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ Preview saved to: {OUTPUT_FILE}")
    print("\nDone! Open experiment_preview.html in your browser to view the preview.")


if __name__ == "__main__":
    main()
