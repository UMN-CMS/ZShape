voigtPlusBKGHFxxbinxx = cms.vstring(
    #"Voigtian::signal(mass, mean[91.2,85,96], width[2.495], sigma[2.3,1,9])",
    '#signal /data/whybee1a/user/haupt/Electrons/TNPTREE10/ALLHFBins.root xxbinxx',
    "EXPR::backgroundPass('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak[91.1876],gamma[0.05, 0.0, 0.1],beta[0.051,0.0,0.2],alpha[62.0,35.0,105.0])",
    "EXPR::backgroundFail('(RooMath::erfc((alpha - mass) * beta))*(( (mass-peak)*gamma < -70  )* (1e20) + ( (mass-peak)*gamma > 70 )* (0.0) + ( (mass-peak)*gamma >= -70 && (mass-peak)*gamma <= 70) * exp(-(mass-peak)*gamma))',mass,peak,gamma,beta,alpha)",
    "efficiency[0.9,0,1]",
    "signalFractionInPassing[0.9]"
    ),
