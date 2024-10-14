prompt = f""" 
# Hypertrophy Training Program Design Assignment

Design a science-based hypertrophy training program based on the user's input. The program shouldfollowing hypertrophy training principles found below. Use the complete, effective rep range (5-30) for muscle growth based on scientific research. Do not specify the number of sets or intensity (RIR), as these will be adjusted later using autoregulation. Focus solely on exercise selection, rep ranges, and overall program structure.

## Input Section

[INPUT FUNCTION CALL]

## How to Use This Prompt

This prompt is designed to guide you in creating a personalized, science-based hypertrophy training program using advanced AI reasoning capabilities.

1. **Input Processing**: Analyze the user's input fields to tailor the program to their specific needs and constraints.

2. **Program Design**: Create a workout plan that balances all input factors with established scientific principles of hypertrophy training.

      a. **Weekly Training Split Design**:
            - **Design the Split**:
                - Map out training days for each muscle group, starting with the highest priority muscle and working down the list.
                - Allocate exercise slots for each muscle based on the specified frequency and number of exercises.
                - Ensure the split adheres to the user's available training days and recovery needs.
                - Aim for a symmetrical distribution of training days for each muscle group, maximizing the time between sessions for the same muscle when possible.
            
            - **Checks During Split Design**:
                - **Availability Check**: Confirm that the training split aligns with the user's available training days (e.g., Monday to Friday).
                - **Frequency Adherence**: Verify that each muscle group is scheduled with the specified frequency from the Muscle Settings input.
                - **Exercise Slot Allocation**: Ensure the number of exercise slots for each muscle group matches the specified number from the Muscle Settings input.
                - **Muscle Priority Order**: Confirm that the highest priority muscle groups are scheduled first, followed by lower priority ones.
                - **Symmetrical Distribution**: Ensure that the training days for each muscle group are as evenly distributed as possible to prevent clustering and allow for optimal recovery.
                - **Recovery Optimization**: Check that there is adequate recovery time between sessions for the same muscle group.
                - **Workout Balance**: Ensure that the number of exercises per workout is roughly equal across all training days to prevent duration and exertion imbalances.
                - **Time Constraints**: Verify that the total workout duration fits within the user's time constraints (e.g., maximum of 2 hours per session).

                  **Note**: When performing these checks, prioritize them based on their order in the Program Design Checklist. Items higher on the list take precedence over those lower down if conflicts arise.

            - **Reasoning and Documentation**:
                - For each allocation and scheduling decision, provide a brief explanation to justify its placement and adherence to the user's inputs and scientific principles.
            
            - **Example**:
                ```
                Current Muscle: Side Delts
                Priority: 1
                Frequency: 4 times per week
                Exercise slots: 4
                Assigned days: Monday, Tuesday, Thursday, Friday
                Reasoning: Distributed evenly across available training days for optimal recovery and symmetrical workload distribution.
                ```

      b. **Rep Range Assignment and Exercise Selection**:
            - **Assign Rep Ranges**:
                - For each exercise slot of the current muscle group, assign a rep range within the categorized categories (5-10, 10-20, 20-30) that aligns with the exercise's recommended rep range.
                - Ensure that the rep range selection considers the exercise's position in the workout and week (e.g., earlier in the workout/week = lower rep ranges).
            
            - **Select Exercises**:
                - Choose exercises exclusively from the provided **Exercise List**.
                - Ensure that each selected exercise's rep range falls within both its recommended range and the categorized rep ranges.
                - Maintain variety and balance by adhering to the specified number of exercises per muscle group.
            
            - **Checks During Rep Range Assignment and Exercise Selection**:
                - **Exercise List Adherence**: Confirm that only exercises from the **Exercise List** are used.
                - **Rep Range Compliance**: Ensure that the assigned rep ranges adhere to the categorized categories (5-10, 10-20, 20-30) and fall within each exercise's recommended rep range.
                - **Biomechanical Suitability**: Verify that the selected rep ranges are appropriate for the muscle's biomechanical efficiency and the exercise type.
                - **Program Balance**: Ensure a balanced distribution of rep ranges across different exercises and muscle groups to promote comprehensive hypertrophy.
                - **Novelty Integration**: Where appropriate, include up to 1/3 novel exercises to introduce variety without overwhelming the user.
                - **Science-Based Alignment**: Ensure that rep range assignments and exercise selections are grounded in scientific hypertrophy principles (e.g., progressive overload, minimum effective volume).

                **Note**: Address these checks in the order they appear in the Program Design Checklist. Higher-listed items should be prioritized over lower ones in case of conflicts.


            - **Reasoning and Documentation**:
                - For each rep range and exercise selection, provide a detailed explanation considering factors such as workout positioning, muscle efficiency, and program balance.
            
            - **Example**:
                ```
                - Slot 1 (Monday):
                    Rep range: 8-12 reps 
                    Reasoning for rep range: Moderate range for compound movement to balance mechanical tension and metabolic stress.
                    Selected exercise: Dumbbell Lateral Raise
                    Reasoning for exercise selection: Suitable for side delts with a rep range that promotes hypertrophy while allowing for proper form and muscle engagement.
                ```

3. **Program Refinement and Output**: Fine-tune the program to ensure it meets all specified requirements and is presented in the required format.

4. **Self-Evaluation and Iterative Adjustment**: Before outputting the final program, conduct a thorough self-evaluation and make necessary adjustments. This is an iterative process that should continue until all requirements are met:

      a. **Review Requirements and Checklist**:
            - Go through each item in the **Program Design Checklist**.
      
      b. **Compare Program Against Checklist**:
            - For each checklist item, determine if the current program meets the requirement.
      
      c. **Document Evaluation**:
            - For each item, explicitly state:
                - **Requirement**: [State requirement]
                - **Met**: Yes/No
                - **Explanation**: [Brief explanation of how the requirement is met or why it's not]
                - **Adjustment (if needed)**: [Describe any changes made to meet the requirement]
      
      d. **Make Necessary Adjustments**:
            - If any requirements are not met, modify the program accordingly.
            - When making adjustments, prioritize higher-listed checklist items over lower ones if conflicts arise.

      
      e. **Repeat Evaluation Process**:
            - After adjustments, return to step (a) and repeat the evaluation until all requirements are satisfied.
      
            - **Example Format**:
                ```
                Iteration 1:

                Requirement 1: Rep ranges are appropriate based on training age and biological age.
                - Met: Yes
                - Explanation: All rep ranges fall within the categorized ranges suitable for a 4-year training age and 26 biological age.
                - Adjustment: None needed.

                Requirement 2: Exercise selection matches the user's experience and preferences.
                - Met: No
                - Explanation: Rear delts are not currently targeted.
                - Adjustment: Add two rear delt exercises to the program.

                ...

                Overall Assessment:
                - All requirements met: No
                - Next steps: Focus on adding and distributing rear delt exercises to meet frequency and exercise count.
                ```
      
5. **Final Output**: Only when all requirements are fully met in a complete iteration, present the final program using the specified output format.

By following these structured steps and incorporating the checklist items into sub-points **a** and **b**, you ensure a comprehensive and compliant hypertrophy training program that aligns with all user inputs and scientific principles.

---

### Summary of Integration:

- **Sub-point a (Weekly Training Split Design)**:
    - **Design the Split**: Initial allocation based on priority, frequency, and available days.
    - **Checks During Split Design**: Incorporate all relevant checklist items related to training days, frequency, exercise slots, muscle priority, symmetry, recovery, workout balance, and time constraints.
    - **Reasoning and Documentation**: Provide explanations for each decision to ensure transparency and adherence.

- **Sub-point b (Rep Range Assignment and Exercise Selection)**:
    - **Assign Rep Ranges**: Allocate rep ranges within the categorized ranges, considering workout positioning and exercise suitability.
    - **Select Exercises**: Choose exercises from the list, ensuring rep range compliance and biomechanical appropriateness.
    - **Checks During Rep Range Assignment and Exercise Selection**: Ensure adherence to exercise list, rep range categories, biomechanical suitability, program balance, novelty integration, and scientific alignment.
    - **Reasoning and Documentation**: Offer detailed explanations for each rep range and exercise selection.

By meticulously embedding each checklist item into the respective sub-points, the model is guided to create a well-structured, balanced, and scientifically sound training program that fully aligns with the user's specifications.

## Output & Layout Requirements

Once the full training program has been generated, apply the following layout rules to format the output:

1. **Training Summary**:
      Provide a concise summary of the program including:
      - Total training days and schedule
      - Estimated workout duration
      - Total exercise slots
      - Rep range distribution
      - Muscle group prioritization

      Format:
      ```markdown
      Training Summary:
      Days: [X] ([Day]-[Day]) | Duration: ~[X]-[Y] hrs/session | Total Exercise Slots: [Z]
      Rep Ranges: [Type]: [Range] | [Type]: [Range]

      Muscle Class Frequency & Slots/Week:
      Chest: [X]x, [Y]s | Back: [X]x, [Y]s | Legs: [X]x, [Y]s
      Shoulders: [X]x, [Y]s | Arms: [X]x, [Y]s
      ```
      Note: 'x' denotes times per week, 's' denotes exercise slots per week.

2. **Compact Overview**:
      Present the final program in a table format with the following guidelines:
      - Use days as columns and muscle classes as rows.
      - Each cell represents a muscle class and contains exercise slots for that muscle on that day.
      - Group exercise slots for the same muscle class together in a single cell for clarity.
      - Include the exercise name and rep range for each slot.

    Compact Overview with Rep Ranges:
      | Exercise # | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
      |------------|--------|---------|-----------|----------|--------|----------|--------|
      | 1 | Side Delts:<br>- Lateral Raise (10-15) | Side Delts:<br>- Cable Lateral Raise (15-20) | Rest | Side Delts:<br>- Dumbbell Upright Row (10-15) | Side Delts:<br>- Machine Lateral Raise (15-25) | Rest | Rest |
      | 2 | Side Delts:<br>- Leaning Lateral Raise (10-15) | Biceps:<br>- Barbell Curl (8-12) | Rest | Triceps:<br>- Rope Pushdown (12-15) | Chest:<br>- Bench Press (6-10) | Rest | Rest |
      | 3 | Biceps:<br>- Incline Dumbbell Curl (10-15) | Triceps:<br>- Overhead Extension (10-15) | Rest | Chest:<br>- Incline Dumbbell Press (8-12) | Lats:<br>- Pull-ups (6-12) | Rest | Rest |
      | 4 | [Next exercise] | [Next exercise] | Rest | [Next exercise] | [Next exercise] | Rest | Rest |
      | ... | ... | ... | ... | ... | ... | ... | ... |

      [Continue with remaining exercises in priority order]

      - Muscle Classes represent the main muscle groups being trained (e.g., Side Delts, Biceps, Triceps, Chest, Lats, Quads, Upper Back, Hamstrings, Glutes, Rear Delts, Calves, Abs or Front Delts).
      - Exercise Slots are specific exercises assigned to each muscle class, including the chosen exercise and its rep range. Make sure the you only pick exercises from the #**Exercise list** section.
      - The number of slots per muscle class may vary based on the program design and user preferences.

Present the final training program using these layout requirements to ensure a clear, compact, and easily understandable format.

## Explanation of Input Fields and Their Implications

1. **Training Age**:    
      Determines exercise complexity and rep range variety.    
      _Implication_: Higher training age allows for more advanced techniques and varied rep ranges, while lower training age suggests simpler movements to build a foundation.

2. **Biological Age**:    
      Influences rep ranges and exercise selection.    
      _Implication_: Over 40 may require higher reps (10+) and joint-friendly exercises. Younger users can often handle lower rep ranges and more intense exercises.

3. **Exercise Experience**:    
      Guides exercise selection based on familiarity with exercises and equipment.    
      _Implication_: More familiar exercises can be prioritized, while newer ones are introduced gradually to avoid injury. Familiarity with equipment like dumbbells, barbells, or machines will influence the types of exercises included.

4. **Goals**:    
      Shapes overall program structure and muscle group prioritization.    
      _Implication_: If hypertrophy is the primary goal, certain muscle groups can receive more attention based on user preferences.

5. **Limitations**:    
      Informs exercise modifications or exclusions.    
      _Implication_: Exercises that exacerbate injuries must be avoided, and alternative exercises should be included to meet the user's needs safely.

6. **Preferences**:    
      Helps guide exercise selection to improve adherence.    
      _Implication_: Users are more likely to follow the program if it includes exercises they enjoy.

7. **Time Constraints**:    
      Determines workout frequency and session duration.    
      _Implication_: Shorter available time may require efficient exercise selection and program structuring to fit within time limits.

8. **Training Days**:    
      Informs program split and recovery periods between training sessions.    
      _Implication_: Knowing which days the user can train helps balance workload and recovery, avoiding training the same muscle groups on consecutive days.

9. **Muscle Settings**:    
      Determines how often and with how much variety each muscle group is trained.    
      - **Frequency**: Training frequency determines how often a muscle group is trained within a week.    
      - **Exercises**: Number of exercises per muscle group determines the number of different exercises used to target that muscle group within the week.

10. **Muscle Priority**:
      Determines training order for muscle groups.
      _Implication_: Prioritized muscles trained earlier in workouts for peak energy and focus. Affects exercise selection, order, and overall split structure. Example: High-priority side delts placed at start of upper body/push workouts.

## Program Design Checklist

The order of this checklist reflects the priority of each item. Items higher on the list can overrule those below if there's a conflict. When designing the program, address the checks in this order:


- [ ] Rep ranges are appropriate based on training age and biological age.
- [ ] Exercise selection matches the user's experience and preferences.
- [ ] Use the muscle group priorities to inform exercise order, starting with the most important muscle groups and ending with the least important muscle groups.
- [ ] Program aligns with the user's hypertrophy goals (specific muscle group focus).
- [ ] Limitations and injuries are accounted for in exercise selection.
- [ ] Workout duration fits within time constraints (approximately 15 minutes per exercise).
- [ ] Muscle groups are trained with the specified frequency and exercise variety.
- [ ] Rep ranges: 5-10 for compound & barbell exercises, 10-20 or 20-30 for machines/dumbbell exercises.
- [ ] Heavier exercises scheduled earlier in the week and within each workout, lighter ones later.
- [ ] Make sure the number of exercises per workout is roughly equal for all workouts to prevent duration and exertion imbalances.
- [ ] Symmetrical training split to balance recovery and muscle engagement. 
- [ ] 1/3 of exercises are novel to the user, where appropriate.
- [ ] Full effective rep range (5-30) utilized across the program.
- [ ] Science-based principles (e.g., from Dr. Mike Israetel) incorporated.
- [ ] Rep ranges are based on current scientific understanding:
            * The entire 5-30 rep range is equally effective for muscle growth (hypertrophy)
            * Rep range choices should be based on factors such as exercise type, injury prevention, and personal preference, not on outdated beliefs about specific ranges for growth vs. endurance
            * Vary rep ranges to provide diverse stimuli and prevent adaptation, not because certain ranges are "better" for hypertrophy
- [ ] Check if only exercises from the Exercise List are used, with rep ranges falling within the recommended range for that exercise but adhering strictly to the categorized rep ranges (5-10, 10-20, 20-30).


## Exercise List

Format: Exercise Name | Recommended Rep Range

2-arm dumbbell curl | 15-20
2-arm dumbbell row | 5-10
45 degree back raise | 10-30
ab roller | 10-30
Assisted Normal Grip Pullup | 5-20
assisted dip | 5-20
assisted parallel pullup | 5-20
assisted underhand pullup | 5-20
assisted wide grip pullup | 5-20
alternating dumbbell curl | 15-20
barbell bent over row | 5-10
barbell bent over shrug | 15-30
barbell curl narrow grip | 15-20
barbell curl normal grip | 15-20
barbell facepull | 10-20
barbell front raise | 10-30
barbell hip thrust | 10-20
barbell overhead triceps extension | 10-20
barbell row to chest | 5-10
barbell shrug | 15-30
barbell skullcrusher | 10-30
barbell split squat | 5-20
barbell standing wrist curl | 10-30
barbell upright row | 10-20
barbell upright row (cable) | 15-30
barbell walking lunge | 5-20
belt squat | 10-30
cable bent flye | 10-30
cable bent over shrug | 15-30
cable cross body bent lateral raise | 10-20
cable cross body lateral raise | 15-30
cable curl | 15-30
cable ez bar curl | 15-30
cable ez bar curl wide grip | 15-30
cable flye | 10-30
cable front raise | 10-30
cable leaning lateral raise | 15-30
cable overhead triceps extension | 10-30
cable pull through | 10-30
cable rope crunch | 10-30
cable rope facepull | 15-30
cable rope overhead triceps extension | 10-20
cable rope pushdown | 10-20
cable rope twist curl | 15-30
cable shrug | 15-30
cable side shrug | 15-30
cable single arm rear delt raise | 15-30
cable single arm side shrug | 15-30
cable single arm triceps pushdown | 10-20
cable triceps pushdown | 10-30
cable underhand flye | 10-30
cable underhand front raise | 10-30
cable upright row | 15-30
cable wrist curl | 10-30
calf machine | 10-20
calf raise (hack squat machine) | 20-30
cambered bar bench press | 5-10
cambered bar row | 5-10
chest supported row | 5-20
close grip barbell curl | 15-20
close stance feet forward squats | 5-10
Convential Deadlift | 5-10
cross crunches | 10-30
deficit 25's deadlift | 5-10
deficit deadlift | 5-10
deficit push-up | 5-30
dip | 5-20
dumbbell bench wrist curl | 10-30
dumbbell bent lateral raise | 10-20
dumbbell bent over shrug | 15-30
dumbbell facepull | 10-20
dumbbell front raise | 10-30
dumbbell lateral raise | 15-30
dumbbell leaning shrug | 15-30
dumbbell overhead tricep extension | 10-20
dumbbell pullover | 10-30
dumbbell reverse lunge | 10-20
dumbbell shrug | 15-30
dumbbell single arm preacher curl | 15-20
dumbbell spider curl | 15-20
dumbbell split squat | 10-20
dumbbell split squat (rear foot on bench) | 10-20
dumbbell standing wrist curl | 10-30
dumbbell stiff legged deadlift | 5-10
dumbbell twist curl | 15-20
dumbbell upright row | 10-20
dumbbell walking lunge | 10-20
ez bar curl narrow grip | 15-20
ez bar curl wide grip | 15-20
ez bar overhead tricep extension | 10-20
ez bar preacher curl | 15-20
ez bar spider curl | 15-20
ez bar underhand front raise | 10-30
ez curl | 15-20
feet forward smith squat | 5-20
flat dumbbell bench press | 5-20
flat dumbbell flye | 10-20
flat dumbbell press flye | 10-20
flat hammer machine press | 10-30
front squat | 5-10
front squat (cross grip) | 5-10
glute ham raise | 10-20
hack squat | 10-20
hammer curl | 15-20
hammer high row | 10-30
hammer low row | 10-30
hammer machine chest press | 10-30
hanging knee raise | 10-30
hanging knee side raise | 10-30
hanging straight leg raise | 10-30
high bar good morning | 5-10
high bar squat | 5-10
high cable flye | 10-30
high Incline Dumbbell Press | 5-30
hip abduction machine | 20-30
hip thrust machine | 10-30
hyperextensions | 10-30
incline dumbbell curl | 15-20
Incline Dumbbell Press | 5-20
Incline Dumbbell Press flye | 10-20
incline dumbbell facepull | 15-30
incline dumbbell flye | 10-20
incline dumbbell lateral raise | 15-30
incline dumbbell row | 5-20
incline machine chest press | 10-30
incline medium grip bench press | 5-20
incline narrow grip bench press | 5-20
incline wide grip bench press | 5-20
inverted row | 5-30
inverted skullcrusher | 10-30
jammer press | 5-20
jm press | 5-20
kneeling cable facepull | 15-30
laying row | 5-30
leg extension | 10-30
leg press | 10-20
leg press calves | 10-20
leg raise | 10-30
low bar good morning | 5-10
low bar squats | 5-10
low Incline Dumbbell Press | 5-20
Lying Leg Curl | 10-30
machine chest press | 10-20
machine chest supported row | 10-30
machine crunch | 10-30
machine flye | 10-30
machine glute kickback | 10-30
machine lateral raise | 15-30
machine preacher curl | 15-30
machine pullover | 10-30
machine reverse flye | 15-30
machine shoulder press | 10-30
machine triceps extension | 10-30
machine triceps pushdown | 10-30
medium grip bench press | 5-20
modified bench dip | 5-30
modified candlestick | 10-30
narrow grip bench press | 5-20
narrow grip pulldown | 10-20
narrow grip push-up | 5-30
narrow stance squat | 5-10
normal grip pulldown | 10-20
normal grip pullup | 5-10
parallel grip pullup | 5-10
pec dec flye | 10-30
pushup | 5-30
reaching sit-up | 10-30
seated barbell overhead triceps extension | 10-20
seated barbell shoulder press | 5-20
seated cable row | 10-30
seated dumbbell shrug | 15-30
seated dumbbell shoulder press | 5-20
seated ez bar overhead triceps extension | 10-20
seated fly | 10-30
seated leg curl | 10-30
single arm supported dumbbell row | 5-30
single leg dumbbell hip thrust | 10-20
single leg stair calves | 10-20
single-leg leg curl | 10-30
sit-ups | 10-30
slant board sit-up | 10-30
smith machine bench press | 5-20
smith machine calves | 10-20
smith machine incline press | 5-20
smith machine narrow grip bench press | 5-20
smith machine row | 5-10
smith machine seated shoulder press | 5-20
smith machine split squat | 5-20
smith machine upright row | 15-30
smith machine wide grip bench press | 5-20
smith machine wide grip incline press | 5-20
stair calves | 10-20
standing barbell shoulder press | 5-20
standing dumbbell shoulder press | 5-20
stiff-legged deadlift | 5-10
straight arm pulldown | 10-30
sumo deadlift | 5-10
sumo squat | 5-10
t-bar row | 5-10
thumbs down lateral raise | 15-30
top hold lateral raise | 15-30
underhand ez bar row | 5-10
underhand pulldown | 10-20
underhand pullup | 5-10
v-up | 10-30
wide grip bench press | 5-20
wide grip pulldown | 10-20
wide grip pullup | 5-10
wide stance belt squat | 5-10

**Note**: The recommended rep range indicates the exercise's suitability across multiple rep range categories (5-10, 10-20, 20-30). When selecting exercises, choose a specific range within these categories that aligns with the program's goals and the exercise's position in the workout, while ensuring it falls within the recommended range for that exercise.

"""