#eos tests
eostest='/eos/experiment/fcc/hh/tests/testfile.lhe.gz'
eostest_size=1312594

#dicts
##LHE dictionnary
lhe_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/LHE_HELHC.json'
##LHE read file true/false
readlhe_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/LHE_HELHC_read.json'


##eos directory for MG5@MCatNLO gridpacks
gp_dir      = '/eos/experiment/fcc/helhc/generation/gridpacks/'
##eos directory for lhe files
lhe_dir     = '/eos/experiment/fcc/helhc/generation/lhe/'
##extension
lhe_ext     ='.lhe.gz'



##FCC events dictionnary
fcc_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphes_VERSION.json'
##FCC versions
fcc_versions=['helhc_v01']
##FCC read file true/false
readfcc_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphes_VERSION_read.json'

##eos directory for FCCSW pythia delphes files
delphes_dir = '/eos/experiment/fcc/helhc/generation/DelphesEvents/'
##extension
delphes_ext='.root'
##name of the ttree
treename='events'

##where the delphes cards are stored
delphescards_dir = '/eos/experiment/fcc/helhc/utils/delphescards/'
##where the pythia cards are stored
pythiacards_dir  = '/eos/experiment/fcc/helhc/utils/pythiacards/'
##where the FCC config script is stored
fccconfig_dir    = '/eos/experiment/fcc/helhc/utils/config/'

##muom momentum delphes resolution card
delphescard_mmr='muonMomentumResolutionVsP.tcl'
##momentum resolution delphes card
delphescard_mr='momentumResolutionVsP.tcl'
##delphes base card
delphescard_base='card.tcl'
##FCC config script name
fccconfig='PythiaDelphes_config_v02.py'

##base dir of FCCSW
fccsw_dir='/cvmfs/fcc.cern.ch/sw/0.8.2/'
##init script for FCCSW
stack=fccsw_dir+'init_fcc_stack.sh'
##FCCSW dir
fccsw=fccsw_dir+'fccsw/0.8.2/x86_64-slc6-gcc62-opt/'

#list of processes only with Pythia, meaning no LHE
pythialist={
'p8_pp_Zprime_2TeV_ll':['2TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','5.276e-2','1.0','1.0'],
'p8_pp_Zprime_4TeV_ll':['4TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','3.778e-3','1.0','1.0'],
'p8_pp_Zprime_6TeV_ll':['6TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','3.778e-3','1.0','1.0'],
'p8_pp_Zprime_8TeV_ll':['8TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','3.778e-3','1.0','1.0'],
'p8_pp_Zprime_10TeV_ll':['10TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','3.778e-3','1.0','1.0'],
'p8_pp_Zprime_12TeV_ll':['12TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','4.749e-5','1.0','1.0'],
'p8_pp_Zprime_14TeV_ll':['14TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','e-4','1.0','1.0'],

'p8_pp_Zprime_2TeV_ttbar':['2TeV Z\' -> ttbar','','','7.6378','1.0','1.0'],
'p8_pp_Zprime_5TeV_ttbar':['5TeV Z\' -> ttbar','','','0.305493','1.0','1.0'],
'p8_pp_Zprime_10TeV_ttbar':['10TeV Z\' -> ttbar','','','0.0175724','1.0','1.0'],
'p8_pp_Zprime_15TeV_ttbar':['15TeV Z\' -> ttbar','','','0.002439429','1.0','1.0'],

'p8_pp_RSGraviton_2TeV_ww':['2TeV Z\' -> WW','','','1.811e1','1.0','1.0'],
'p8_pp_RSGraviton_5TeV_ww':['5TeV Z\' -> WW','','','2.892e-1','1.0','1.0'],
'p8_pp_RSGraviton_10TeV_ww':['10TeV Z\' -> WW','','','7.686e-3','1.0','1.0'],
'p8_pp_RSGraviton_15TeV_ww':['15TeV Z\' -> WW','','','7.386e-4','1.0','1.0'],


}


##list of possible decays of LHE files

decaylist = {
'mg_pp_h012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_hh01j_5f':['hhaabb'],
'mg_pp_vbf_h01j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau', 'hnunununu'],
'mg_pp_tth01j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_vh012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_v0123j_5f':['znunu'],
'mg_pp_z0123j_4f':['zll'],
'mg_pp_w0123j_4f':['wlv'],
'mg_pp_ttz_5f':['znunu'],
'mg_pp_hh_lambda050_5f':['haa'],
'mg_pp_hh_lambda090_5f':['haa'],
'mg_pp_hh_lambda095_5f':['haa'],
'mg_pp_hh_lambda100_5f':['haa'],
'mg_pp_hh_lambda105_5f':['haa'],
'mg_pp_hh_lambda110_5f':['haa'],
'mg_pp_hh_lambda150_5f':['haa'],
'mg_pp_hhj_lambda090_5f':['hhbbbb'],
'mg_pp_hhj_lambda095_5f':['hhbbbb'],
'mg_pp_hhj_lambda100_5f':['hhbbbb'],
'mg_pp_hhj_lambda105_5f':['hhbbbb'],
'mg_pp_hhj_lambda110_5f':['hhbbbb'],
'mg_pp_hhj_lambda150_5f':['hhbbbb'],
'mg_pp_hhj_lambda050_5f':['hhbbbb'],

}



##list of decays branching ratios 
# from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR 
# and Particle data Group

branching_ratios = {
'hmumu':2.176E-04,
'haa':2.270E-03,
'hlla':1.533E-03*(3.363E-02 + 3.366E-02),
'hllll':1.240E-04,
'hlvlv':1.055E-02,
'hbb':5.824E-01,
'htautau':6.272E-02,
'zll':0.307,
'wlv':3*0.108,
'hhaabb':2*2.270E-03*5.824E-01,
'hhbbbb':5.824E-01*5.824E-01,
'znunu':0.205,
}


##Gridpack list for MG5@MC@NLO
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

gridpacklist = {
'mg_pp_ee_lo':['','inclusive','','0.000621','1.0','1.0'],
'mg_pp_mumu_lo':['','inclusive','','0.000621','1.0','1.0'],
'mg_pp_tt_lo':['','inclusive','','11.09','1.0','1.0'],
'mg_pp_jj_lo':['','inclusive','','3871','1.0','1.0'],
'mg_pp_vv_lo':['','inclusive','','0.1562','1.0','1.0'],
'mg_pp_vj_lo':['','inclusive','','18.54','1.0','1.0'],

}

