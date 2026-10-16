from pathlib import Path
import sys,json
from PIL import Image,ImageDraw
sys.path.insert(0,'<external-work-pets-scripts>')
from render_animation_previews import ROW_DURATIONS,save_preview
R=Path('.'); a=Image.open(R/'final/spritesheet-extended.png').convert('RGBA'); root=R/'final/encoded-frames'; root.mkdir(exist_ok=True); out=R/'final/previews'; out.mkdir(exist_ok=True)
seq=[]; times=[]; cells={}
for row,(s,ds) in enumerate(ROW_DURATIONS.items()):
 (root/s).mkdir(exist_ok=True); cells[s]=[]
 for col,d in enumerate(ds):
  c=a.crop((col*192,row*208,(col+1)*192,(row+1)*208)); c.save(root/s/f'{col:02}.png');cells[s].append(c)
  bg=Image.new('RGBA',(384,456),'#f7f5f0'); bg.alpha_composite(c.resize((384,416),Image.Resampling.LANCZOS),(0,20)); ImageDraw.Draw(bg).text((12,438),s,fill='#444444');seq.append(bg.convert('RGB'));times.append(d)
save_preview(seq,times,out/'snoopy-all-states.gif')
transition=cells['idle']+cells['jumping']+cells['idle'];dur=ROW_DURATIONS['idle']+ROW_DURATIONS['jumping']+ROW_DURATIONS['idle'];save_preview(transition,dur,out/'snoopy-idle-jump-idle.gif')
look=[a.crop(((i%8)*192,(9+i//8)*208,(i%8+1)*192,(10+i//8)*208)) for i in range(16)];save_preview(look,[160]*16,out/'snoopy-look-loop.gif')
stills=[('Idle',cells['idle'][0]),('Wave',cells['waving'][2]),('Jump',cells['jumping'][2]),('Thinking',cells['running'][2])]
sheet=Image.new('RGB',(768,240),'#f7f5f0');dr=ImageDraw.Draw(sheet)
for i,(label,c) in enumerate(stills):sheet.paste(c,(i*192,18),c);dr.text((i*192+12,225),label,fill='#444444')
sheet.save(out/'snoopy-motion-stills.png')
print(out)
