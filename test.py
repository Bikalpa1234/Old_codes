from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
        self.all_sol=[]

    def on_solution_callback(self):
        self.__solution_count += 1
        l=[self.Value(u) for u in self.__variables]
        self.all_sol.append(l)

    def solution_count(self):
        return self.__solution_count


def mix():
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

    model.AddLinearConstraint(aa*10 +ab*15 +ac*20 +ad *25 +ae*40 +af*13, -100,208)
    model.AddLinearConstraint(ba*10 +bb*15 +bc*20 +bd *25 +be*40 +bf*13,-100,208)
    model.AddLinearConstraint(ca*10 +cb*15 +cc*20 +cd *25 +ce*40 +cf*13,-100,156)
    model.AddLinearConstraint(da*10 +db*15 +dc*20 +dd *25 +de*40 +df*13,-100,208)
    model.AddLinearConstraint(ea*10 +eb*15 +ec*20 +ed *25 +ee*40 +ef*13,-100,104)
    model.AddLinearConstraint(fa*10 +fb*15 +fc*20 +fd *25 +fe*40 +ff*13,-100,156)
    model.AddLinearConstraint(ga*10 +gb*15 +gc*20 +gd *25 +ge*40 +gf*13,-100,104)
    model.AddLinearConstraint(ha*10 +hb*15 +hc*20 +hd *25 +he*40 +hf*13,-100,130)
    model.AddLinearConstraint(ia*10 +ib*15 +ic*20 +id *25 +ie*40 +iaf*13,-100,208)
    model.AddLinearConstraint(ja*10 +jb*15 +jc*20 +jd *25 +je*40 +jf*13,-100,104)
    model.AddLinearConstraint(ka*10 +kb*15 +kc*20 +kd *25 +ke*40 +kf*13,-100,104)
    model.AddLinearConstraint(la*10 +lb*15 +lc*20 +ld *25 +le*40 +lf*13,-100,208)

    model.Add(aa +ba +ca +da +ea +fa +ga +ia +ja +ka +la ==16)
    model.Add(ab +bb +cb +db +eb +fb +gb +ib +jb +kb +lb ==52)
    model.Add(ac +bc +cc +dc +ec +fc +gc +ic +jc +kc +lc ==5)
    model.Add(ad +bd +cd +dd +ed +fd +gd +id +jd +kd +ld ==15)
    model.Add(ae +be +ce +de +ee +fe +ge +ie +je +ke +le ==8)
    model.Add(af +bf +cf +df +ef +ff +gf +iaf +jf +kf +lf ==12)


    solver=cp_model.CpSolver()

    sol_printer=VarArraySolutionPrinter(var)

    solver=cp_model.CpSolver()
    status=solver.SearchForAllSolutions(model, sol_printer)
    return sol_printer.all_sol

