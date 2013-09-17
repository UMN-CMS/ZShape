voigtPlusBKGHFpt0eta0 = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root pt0eta0',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.015140],beta[0.115100],alpha[51.570000])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
voigtPlusBKGHFpt1eta0 = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root pt1eta0',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.009006],beta[0.065720],alpha[68.050003])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
voigtPlusBKGHFpt0eta1 = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root pt0eta1',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.100000],beta[0.062200],alpha[88.379997])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
voigtPlusBKGHFpt1eta1 = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root pt1eta1',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.000003],beta[0.230000],alpha[64.940002])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
voigtPlusBKGHFpt0eta2 = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root pt0eta2',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.014850],beta[0.114300],alpha[51.529999])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
voigtPlusBKGHFpt1eta2 = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root pt1eta2',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.009377],beta[0.061220],alpha[68.900002])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
