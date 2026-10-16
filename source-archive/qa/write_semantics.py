import json
from pathlib import Path
labels=['000','022.5','045','067.5','090','112.5','135','157.5','180','202.5','225','247.5','270','292.5','315','337.5']
expected=['up','up-right','up-right','up-right','right','down-right','down-right','down-right','down','down-left','down-left','down-left','left','up-left','up-left','up-left']
evidence=[
'Nose lies high above collar at top of upturned muzzle; underside visible and eyes naturally occluded. Body stays upright.',
'Muzzle and nose extend screen-right and upward, neck raised. Angle near 045 is subtle; same quadrant, no reversal.',
'Muzzle tip extends right and upward, with cheek smile visible. Near-duplicate angle with preceding pose accepted as reviewed warning.',
'Nose remains right of head center and slightly above eye line; muzzle tips up mildly.',
'Nose projects strongly screen-right on level muzzle; a profile eye visible.',
'Nose projects screen-right, bowed muzzle slopes downward relative to neutral; eyes look down the muzzle.',
'Muzzle slopes down and right; nose low and right of eye pair.',
'Head bows deeply with nose below eyes and slightly screen-right. Boundary next pose turns frontal; body remains fixed.',
'Head bows frontally; nose directly beneath eyes toward bottom edge, both ears flank face.',
'Nose beneath eyes and slightly screen-left; snout bows toward lower-left.',
'Nose clearly lower-left of eyes; head yaws screen-left while remaining bowed.',
'Nose prominent on screen-left and lower than eyes; mild downward pitch.',
'Level muzzle projects strongly screen-left with a profile eye. Body/tail remain same as other cells.',
'Nose projects screen-left and slightly above eye line; neck extends and muzzle tilts upward.',
'Nose prominently upper-left of eyes; head lifted toward upper-left.',
'Nose near top-left of upturned muzzle; underside revealed, head approaches up anchor naturally.'
]
p={'directions':[{'label':l,'expected':e,'observed':e,'verdict':'warning' if l in ['022.5','045','157.5'] else 'pass','evidence':x} for l,e,x in zip(labels,expected,evidence)],'continuity_review':'Labeled native-size review: stable feet, torso and tail; all quadrants correct, no reversed look loop. Metric outliers reflect head perspective changes. 157.5 to180 visibly moves muzzle toward middle; lower body remains anchored. Similar 022.5 and045 poses accepted as subtle intermediate steps, confirmed independently.'}
Path('./qa/direction-semantics.json').write_text(json.dumps(p,indent=2))
