import numpy as np
from ortools.sat.python import cp_model

model=cp_model.CpModel()

aa=model.NewIntVar(-100,100, 'aa')
ab=model.NewIntVar(-100,100, 'ab')
ac=model.NewIntVar(-100,100, 'ac')
ad=model.NewIntVar(-100,100, 'ad')
ae=model.NewIntVar(-100,100, 'ae')
af=model.NewIntVar(-100,100, 'af')


ba=model.NewIntVar(-100,100, 'ba')
bb=model.NewIntVar(-100,100, 'bb')
bc=model.NewIntVar(-100,100, 'bc')
bd=model.NewIntVar(-100,100, 'bd')
be=model.NewIntVar(-100,100, 'be')
bf=model.NewIntVar(-100,100, 'bf')

ca=model.NewIntVar(-100,100, 'ca')
cb=model.NewIntVar(-100,100, 'cb')
cc=model.NewIntVar(-100,100, 'cc')
cd=model.NewIntVar(-100,100, 'cd')
ce=model.NewIntVar(-100,100, 'ce')
cf=model.NewIntVar(-100,100, 'cf')

da=model.NewIntVar(-100,100, 'da')
db=model.NewIntVar(-100,100, 'db')
dc=model.NewIntVar(-100,100, 'dc')
dd=model.NewIntVar(-100,100, 'dd')
de=model.NewIntVar(-100,100, 'de')
df=model.NewIntVar(-100,100, 'df')

ea=model.NewIntVar(-100,100, 'ea')
eb=model.NewIntVar(-100,100, 'eb')
ec=model.NewIntVar(-100,100, 'ec')
ed=model.NewIntVar(-100,100, 'ed')
ee=model.NewIntVar(-100,100, 'ee')
ef=model.NewIntVar(-100,100, 'ef')

fa=model.NewIntVar(-100,100, 'fa')
fb=model.NewIntVar(-100,100, 'fb')
fc=model.NewIntVar(-100,100, 'fc')
fd=model.NewIntVar(-100,100, 'fd')
fe=model.NewIntVar(-100,100, 'fe')
ff=model.NewIntVar(-100,100, 'ff')

ga=model.NewIntVar(-100,100, 'ga')
gb=model.NewIntVar(-100,100, 'gb')
gc=model.NewIntVar(-100,100, 'gc')
gd=model.NewIntVar(-100,100, 'gd')
ge=model.NewIntVar(-100,100, 'ge')
gf=model.NewIntVar(-100,100, 'gf')

ha=model.NewIntVar(-100,100, 'ha')
hb=model.NewIntVar(-100,100, 'hb')
hc=model.NewIntVar(-100,100, 'hc')
hd=model.NewIntVar(-100,100, 'hd')
he=model.NewIntVar(-100,100, 'he')
hf=model.NewIntVar(-100,100, 'hf')

ia=model.NewIntVar(-100,100, 'ia')
ib=model.NewIntVar(-100,100, 'ib')
ic=model.NewIntVar(-100,100, 'ic')
id=model.NewIntVar(-100,100, 'id')
ie=model.NewIntVar(-100,100, 'ie')
iaf=model.NewIntVar(-100,100, 'iaf')

ja=model.NewIntVar(-100,100, 'ja')
jb=model.NewIntVar(-100,100, 'jb')
jc=model.NewIntVar(-100,100, 'jc')
jd=model.NewIntVar(-100,100, 'jd')
je=model.NewIntVar(-100,100, 'je')
jf=model.NewIntVar(-100,100, 'jf')

ka=model.NewIntVar(-100,100, 'ka')
kb=model.NewIntVar(-100,100, 'kb')
kc=model.NewIntVar(-100,100, 'kc')
kd=model.NewIntVar(-100,100, 'kd')
ke=model.NewIntVar(-100,100, 'ke')
kf=model.NewIntVar(-100,100, 'kf')

la=model.NewIntVar(-100,100, 'la')
lb=model.NewIntVar(-100,100, 'lb')
lc=model.NewIntVar(-100,100, 'lc')
ld=model.NewIntVar(-100,100, 'ld')
le=model.NewIntVar(-100,100, 'le')
lf=model.NewIntVar(-100,100, 'lf')


var=[aa,ab,ac,ad,ae,af,aa,ab,ac,ad,ae,af,ba,bb,bc,bd,be,bf,ca,cb,cc,cd,ce,cf,da,db,dc,dd,de,df,ea,eb,ec,ed,ee,ef,fa,fb,fc,fd,fe,ff,ga,gb,gc,gd,ge,gf,ha,hb,hc,hd,he,hf,ia,ib,ic,id,ie,iaf,ja,jb,jc,jd,je,jf,ka,kb,kc,kd,ke,kf,la,lb,lc,ld,le,lf]

model.Add(aa*10 +ab*15 +ac*20 +ad *25 +ae*40 +af*20 <=208)
model.Add(ba*1 +bb*1.5 +bc*2 +bd *2.5 +be*4 +bf*2 <=20.8)
model.Add(ca*1 +cb*1.5 +cc*2 +cd *2.5 +ce*4 +cf*2 <=15.6)
model.Add(da*1 +db*1.5 +dc*2 +dd *2.5 +de*4 +df*2 <=20.8)
model.Add(ea*1 +eb*1.5 +ec*2 +ed *2.5 +ee*4 +ef*2 <=10.4)
model.Add(fa*1 +fb*1.5 +fc*2 +fd *2.5 +fe*4 +ff*2 <=15.6)
model.Add(ga*1 +gb*1.5 +gc*2 +gd *2.5 +ge*4 +gf*2 <=10.4)
model.Add(ha*1 +hb*1.5 +hc*2 +hd *2.5 +he*4 +hf*2 <=13)
model.Add(ia*1 +ib*1.5 +ic*2 +id *2.5 +ie*4 +iaf*2 <=20.8)
model.Add(ja*1 +jb*1.5 +jc*2 +jd *2.5 +je*4 +jf*2 <=10.4)
model.Add(ka*1 +kb*1.5 +kc*2 +kd *2.5 +ke*4 +kf*2 <=10.4)
model.Add(la*1 +lb*1.5 +lc*2 +ld *2.5 +le*4 +lf*2 <=20.8)

model.Add(aa +ba +ca +da +ea +fa +ga +ia +ja +ka +la ==16)
model.Add(ab +bb +cb +db +eb +fb +gb +ib +jb +kb +lb ==52)
model.Add(ac +bc +cc +dc +ec +fc +gc +ic +jc +kc +lc ==5)
model.Add(ad +bd +cd +dd +ed +fd +gd +id +jd +kd +ld ==15)
model.Add(ae +be +ce +de +ee +fe +ge +ie +je +ke +le ==8)
model.Add(af +bf +cf +df +ef +ff +gf +iaf +jf +kf +lf ==12)


solver=cp_model.CpSolver()


status=solver.Solve(model)
if status==cp_model.OPTIMAL:
    print('obj value = {}'.format(solver.ObjectiveValue()))
    print("""
         a={}
         b={}
         c={}
         d={}
         """.format(solver.Value(aa),
            solver.Value(ab), 
            solver.Value(ac), 
            solver.Value(ad),
            solver.Value(ae),
            solver.Value(af),
            solver.Value(ba),
            solver.Value(bb), 
            solver.Value(bc), 
            solver.Value(bd),
            solver.Value(be),
            solver.Value(bf),
            solver.Value(ca),
            solver.Value(cb), 
            solver.Value(cc), 
            solver.Value(cd),
            solver.Value(ce),
            solver.Value(cf),
            solver.Value(da),
            solver.Value(db), 
            solver.Value(dc), 
            solver.Value(dd),
            solver.Value(de),
            solver.Value(df),
            solver.Value(ea),
            solver.Value(eb), 
            solver.Value(ec), 
            solver.Value(ed),
            solver.Value(ee),
            solver.Value(ef),
            solver.Value(fa),
            solver.Value(fb), 
            solver.Value(fc), 
            solver.Value(fd),
            solver.Value(fe),
            solver.Value(ff),
            solver.Value(ga),
            solver.Value(gb), 
            solver.Value(gc), 
            solver.Value(gd),
            solver.Value(ge),
            solver.Value(gf),
            solver.Value(ha),
            solver.Value(hb), 
            solver.Value(hc), 
            solver.Value(hd),
            solver.Value(he),
            solver.Value(hf),
            solver.Value(ia),
            solver.Value(ib), 
            solver.Value(ic), 
            solver.Value(id),
            solver.Value(ie),
            solver.Value(iaf),
            solver.Value(ja),
            solver.Value(jb), 
            solver.Value(jc), 
            solver.Value(jd),
            solver.Value(je),
            solver.Value(jf),
            solver.Value(ka),
            solver.Value(kb), 
            solver.Value(kc), 
            solver.Value(kd),
            solver.Value(ke),
            solver.Value(kf),
            solver.Value(la),
            solver.Value(lb), 
            solver.Value(lc), 
            solver.Value(ld),
            solver.Value(le),
            solver.Value(lf),
            ))














