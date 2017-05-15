from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

from DSAregenK import DSAregenK     # <-- where the magic happens

import logging
LOG = logging.getLogger('DSAregenK')
LOG.setLevel(logging.DEBUG)
logging.debug("-- on --")    

privkey = DSA.generate(1024)        # generate new privkey
pubkey  = privkey.publickey()        # extract pubkey

# set the public key values from what we were given
pubkey.p = int('df633b7301871415bef5017d0c0910c7072222433a309d69ffd012f9d3e208e4d31ebdfd0aa30dfb4a7d13ef7832d363d855e2169df89e60acbfc4137a59c3945eb494650913b6087f2e2700eb3b4294eb4377e9cea6d35ddf232519624cc3bd1e7e534aa9379ded37ff6ddff10758124250e3e5a40a1f789f2c0cc16cb96e0f5261b98b01689dbad6f62842a6c3365fcf25fd3def7baad7bfd99bd70dbe067a5b2af7737caba77787537f1c406338b1c3b86c3875563a03024156bf92a6c770010c63e123a0b2b4661970bf522034ea1e376406c5194c5bb82d1c69d77dcca4b8e04d4a347fcc5bd8c91504458c0eb086a0bf10fa7cc8caa11af2e22f32d06f', 16)

pubkey.q = int('9f3710274717b060dee9fef0aaf01572e9cc53ba6ac10492bd5446bb41a248a9',16)

pubkey.g = int('93b411063c7d3b82189c7ea2624be9087a6e40e79020801367a9bc13012630ae2778244492cca9cd86a07dee31163713a2623f3c418b19e7e8fb3ba5e2db359cc6e5efa1c35c37a16bb2dbfe7c8b6bb123bd26a8f299acdd5c6886748d3db1ffa5ce439571de7efac3482ebf5b4a45324963d99506af9e210988c0a26c443659172df05e094572421ca1c5005f4a1650081c532663dd0e5812f4b8ea43f6cdca317755aac3c3f63754be18c0063b919a7a547cb04d44dba2f67154339eaddfadbd8398c94ba5565d7a2d07c1d20e39befee427346e630f5f72176444fed7d8314ca7c472261f8311974da2ddcafab1ee63c6c7377e7592161e1d31b32abaa3bd', 16)

pubkey.y =20636836524380396244196072696577569262126621637693518417515831389588156010110727694179220341766312812167934840038173702512714672935256591366304513258964123770331403988242338829851121917054712366378000466271493525015744412519308988145299857577333546970037261427973290256403898499766279180979277265983341722384272524689611144938145070671581385845523894185215290296247151150557881827136342152143825772770126693742120775894397288900938364960208586264826886039992581043142765638948169372930513082826136892625732961853419727731657648155505907704183872630951714970690302024937399383304248276584035831599631104415986634886780

#Loading Solo Fortress 2
r1 = 65409437784982297110912581342752010737235883633264011939488505540228075281368
s1 = 35423112485595204833342827083528820396508701138465506923287226062770205121840
h1 = 23774880964385620814468110570038093688231692900518718595797672264122586266881

#Loading Miniman XV
r2 = 65409437784982297110912581342752010737235883633264011939488505540228075281368
s2 = 20262912165800849185854645367293864271318988525533982539211381770687917054877
h2 = 47249939200444390154785799101848744001405884122924422864032756950934263851831

a = DSAregenK(pubkey=pubkey)        # feed pubkey 

a.add( (r1,s1),h1 )                    # add signed messages
a.add( (r2,s2),h2 )                    # add signed messages
    
for re_privkey in a.run(asDSAobj=True):     # reconstruct privatekey from samples (needs at least 2 signed messages with equal r param)
    LOG.info( "Reconstructed private_key: %s"%repr(re_privkey))



