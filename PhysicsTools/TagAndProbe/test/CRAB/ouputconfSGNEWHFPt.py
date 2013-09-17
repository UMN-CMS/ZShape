voigtPlusBKGHFpt0 = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root pt0',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.014990],beta[0.114600],alpha[51.549999])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
voigtPlusBKGHFpt1 = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root pt1',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.009178],beta[0.063410],alpha[68.459999])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
