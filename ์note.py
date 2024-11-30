# -*- coding: utf-8 -*-
"""์note

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SCJ-a-mqXeytOY0AKFds08PfK61mBoGs

# Coding Exercise for PMU-B Coding AI - Code Clone Detector

In this coding exercise, you will try using code2vec to generate code vectors from code snippets and find similar code snippets by using cosine similarity. Please follow the steps below.

1. Move the main working folder.
"""

cd /content

"""2. Clone the code2vec project to this working folder."""

!git clone https://github.com/tech-srl/code2vec.git

"""3. Clone the test data to this working folder."""

!git clone https://github.com/cragkhit/PMUB-CodingAI-CloneData.git

"""3. Download the pre-trained code2vec model."""

!wget https://s3.amazonaws.com/code2vec/model/java14m_model.tar.gz
!tar -xvzf java14m_model.tar.gz

"""4. Go inside the code2vec project."""

cd code2vec/

"""5. Try running code2vec to generate a code vector from the given Input.java file."""



!python3 code2vec.py --load /content/models/java14_model/saved_model_iter8.release --predict --export_code_vectors

"""6. We'll start creating code vectors of multiple code snippets."""

cv1 = '0.2585543 0.018499821 0.6259956 -0.91153747 0.28625304 -0.20867313 -0.6456262 -0.5417256 0.40780866 0.6872428 0.48593658 0.8046063 -0.058023423 0.9426887 0.50868416 -0.7689812 -0.048711807 0.8145132 0.90576255 -0.4059241 -0.74391127 0.48965168 0.8245069 -0.828656 -0.18502949 0.7901077 0.8317792 0.05958824 -0.41710785 -0.36823994 -0.8146068 0.96380293 -0.3221373 -0.09550524 0.23637187 -0.7828237 0.41440326 0.85837746 0.7160746 0.42710906 0.86026746 0.3378421 -0.70190024 0.7926471 0.056065813 -0.13136554 0.3117843 0.95096815 0.7354833 -0.82368445 -0.8954565 0.9326848 -0.3107828 0.9633174 0.72925025 0.47538608 -0.15830268 -0.26773548 -0.3451479 0.9110292 -0.9704323 0.89245063 -0.36032683 -0.8097078 0.75253177 -0.4276203 -0.794744 -0.82304156 -0.6887814 0.710863 0.56362087 -0.6238218 -0.8751205 -0.3165001 0.6918507 -0.1842415 -0.45120537 0.29107818 -0.5739533 0.73044753 0.3992608 -0.922578 0.988397 0.2824617 -0.8427991 0.38545176 0.4091736 -0.80609953 -0.5241765 -0.632769 -0.33627385 -0.59111744 0.7637336 -0.69234073 0.79987144 -0.67139256 0.52384675 0.8215902 0.26926327 0.39738202 0.7637237 0.908195 -0.06851485 0.45429832 0.45621157 -0.44760495 -0.83066213 0.660655 -0.8885989 0.9643333 0.91159624 -0.19610572 -0.6570193 0.9189955 0.6287755 0.6763586 0.57360035 0.8044622 0.15594709 0.86987257 0.74620265 0.12886605 -0.571202 -0.5838734 -0.86150956 -0.14513662 0.40013415 -0.8301816 -0.51929915 -0.030817315 -0.7183518 0.8380968 0.8911851 0.24828035 0.32295215 -0.71240085 0.09927705 0.6977972 -0.36181659 0.15715513 -0.37333328 -0.31196588 0.38934436 -0.92469656 -0.69620156 0.3070417 0.75838226 0.6762587 0.95085883 -0.17747968 0.8302594 -0.7904814 0.009289354 -0.6270039 0.70603025 -0.86139053 0.4391611 -0.49321458 0.11893147 0.35378498 -0.26304317 0.82954895 -0.7937252 -0.8962824 0.014315069 0.94419086 0.31369257 0.8396486 -0.90516067 -0.8517296 0.5741993 0.09025121 0.32149994 -0.407448 -0.8138652 -0.94876003 -0.90316546 0.04230091 0.88919353 0.862079 -0.8170335 -0.2836635 0.29817367 0.4657278 -0.8624352 -0.2972049 0.89199436 0.7192866 0.13736606 -0.45771334 0.42584896 -0.8733409 -0.5144834 0.8192859 -0.30608574 -0.7988642 0.8505364 0.2875224 -0.50170493 -0.52384514 -0.80618596 0.6278152 -0.3438828 0.76336145 -0.75226545 -0.8722351 -0.52575326 -0.14364785 -0.31351382 0.8801849 -0.7223246 -0.3271227 0.33801383 0.3105849 -0.7285458 0.8984863 0.5779065 0.8268541 -0.6937938 -0.98829794 0.21864174 0.81059694 -0.8732749 -0.7421322 -0.9170898 0.9027747 0.82607317 0.3975584 0.9220383 -0.28386205 0.4383269 0.67996085 0.4448021 -0.6450141 -0.9438198 0.86594975 -0.3293671 -0.2583968 -0.578713 0.7339607 0.9436058 -0.7429227 0.19106603 0.50790286 0.2600407 -0.90505517 0.44768518 0.26051855 -0.28993964 -0.7989353 -0.7382976 -0.18344407 -0.92704785 -0.7546607 0.7690079 -0.24674131 0.2615453 0.5772341 -0.748982 0.5510926 0.8089032 0.40525544 -0.76406324 0.3939547 0.79505825 0.5367366 -0.70995283 -0.4599514 -0.2620981 -0.6711366 0.63875073 -0.44605744 0.89179 0.8342139 -0.7565692 -0.78562224 0.7342141 0.8891383 -0.090930864 -0.49500078 0.8654859 -0.13922471 -0.49759448 -0.18394092 -0.87766623 -0.7410369 0.10621585 0.5244047 0.37844017 0.024058223 0.78752095 0.3618247 0.80900633 -0.47821358 0.7984024 -0.9058888 -0.8554216 -0.9068364 -0.35494846 -0.84319997 -0.6036904 0.9042927 0.091635376 -0.11074327 -0.025732026 0.6881312 -0.590453 0.29746282 -0.81246763 -0.60796344 -0.68722814 0.85283047 0.08159642 -0.8570137 -0.85794216 0.67010206 -0.41879058 0.44067448 0.8596295 0.43799293 -0.7416377 0.9268815 -0.1297234 0.23661724 0.48412475 0.67597175 0.9079261 -0.52665836 0.9106679 -0.102124974 -0.15129551 -0.10762298 -0.82400084 0.53838515 0.8150033 -0.63103 -0.043885425 0.0879776 0.42031255 0.8096905 -0.8219237 -0.8045856 0.57258767 0.6340139 -0.08463316 -0.7049768 0.8687426 0.46703827 -0.70616174 0.7590643 0.6358374 0.7428731 0.86755216 0.7167369 0.88154966 0.5573708 0.7230853 0.8245705 0.9620808 -0.3535139 0.981297 -0.30206078 0.80207324 0.20489988 0.77773166 0.85460097 -0.8102501 -0.556245 0.8425517 0.26068026 -0.58346665 -0.944479 -0.10337639 0.8890872 0.764282 -0.13533656 -0.90390754 0.3122697 -0.7101809 -0.45474708 -0.6176752 -0.90628725 -0.50176287 -0.6154723'.split(' ')
cv2 = '0.2585543 0.018499821 0.6259956 -0.91153747 0.28625304 -0.20867313 -0.6456262 -0.5417256 0.40780866 0.6872428 0.48593658 0.8046063 -0.058023423 0.9426887 0.50868416 -0.7689812 -0.048711807 0.8145132 0.90576255 -0.4059241 -0.74391127 0.48965168 0.8245069 -0.828656 -0.18502949 0.7901077 0.8317792 0.05958824 -0.41710785 -0.36823994 -0.8146068 0.96380293 -0.3221373 -0.09550524 0.23637187 -0.7828237 0.41440326 0.85837746 0.7160746 0.42710906 0.86026746 0.3378421 -0.70190024 0.7926471 0.056065813 -0.13136554 0.3117843 0.95096815 0.7354833 -0.82368445 -0.8954565 0.9326848 -0.3107828 0.9633174 0.72925025 0.47538608 -0.15830268 -0.26773548 -0.3451479 0.9110292 -0.9704323 0.89245063 -0.36032683 -0.8097078 0.75253177 -0.4276203 -0.794744 -0.82304156 -0.6887814 0.710863 0.56362087 -0.6238218 -0.8751205 -0.3165001 0.6918507 -0.1842415 -0.45120537 0.29107818 -0.5739533 0.73044753 0.3992608 -0.922578 0.988397 0.2824617 -0.8427991 0.38545176 0.4091736 -0.80609953 -0.5241765 -0.632769 -0.33627385 -0.59111744 0.7637336 -0.69234073 0.79987144 -0.67139256 0.52384675 0.8215902 0.26926327 0.39738202 0.7637237 0.908195 -0.06851485 0.45429832 0.45621157 -0.44760495 -0.83066213 0.660655 -0.8885989 0.9643333 0.91159624 -0.19610572 -0.6570193 0.9189955 0.6287755 0.6763586 0.57360035 0.8044622 0.15594709 0.86987257 0.74620265 0.12886605 -0.571202 -0.5838734 -0.86150956 -0.14513662 0.40013415 -0.8301816 -0.51929915 -0.030817315 -0.7183518 0.8380968 0.8911851 0.24828035 0.32295215 -0.71240085 0.09927705 0.6977972 -0.36181659 0.15715513 -0.37333328 -0.31196588 0.38934436 -0.92469656 -0.69620156 0.3070417 0.75838226 0.6762587 0.95085883 -0.17747968 0.8302594 -0.7904814 0.009289354 -0.6270039 0.70603025 -0.86139053 0.4391611 -0.49321458 0.11893147 0.35378498 -0.26304317 0.82954895 -0.7937252 -0.8962824 0.014315069 0.94419086 0.31369257 0.8396486 -0.90516067 -0.8517296 0.5741993 0.09025121 0.32149994 -0.407448 -0.8138652 -0.94876003 -0.90316546 0.04230091 0.88919353 0.862079 -0.8170335 -0.2836635 0.29817367 0.4657278 -0.8624352 -0.2972049 0.89199436 0.7192866 0.13736606 -0.45771334 0.42584896 -0.8733409 -0.5144834 0.8192859 -0.30608574 -0.7988642 0.8505364 0.2875224 -0.50170493 -0.52384514 -0.80618596 0.6278152 -0.3438828 0.76336145 -0.75226545 -0.8722351 -0.52575326 -0.14364785 -0.31351382 0.8801849 -0.7223246 -0.3271227 0.33801383 0.3105849 -0.7285458 0.8984863 0.5779065 0.8268541 -0.6937938 -0.98829794 0.21864174 0.81059694 -0.8732749 -0.7421322 -0.9170898 0.9027747 0.82607317 0.3975584 0.9220383 -0.28386205 0.4383269 0.67996085 0.4448021 -0.6450141 -0.9438198 0.86594975 -0.3293671 -0.2583968 -0.578713 0.7339607 0.9436058 -0.7429227 0.19106603 0.50790286 0.2600407 -0.90505517 0.44768518 0.26051855 -0.28993964 -0.7989353 -0.7382976 -0.18344407 -0.92704785 -0.7546607 0.7690079 -0.24674131 0.2615453 0.5772341 -0.748982 0.5510926 0.8089032 0.40525544 -0.76406324 0.3939547 0.79505825 0.5367366 -0.70995283 -0.4599514 -0.2620981 -0.6711366 0.63875073 -0.44605744 0.89179 0.8342139 -0.7565692 -0.78562224 0.7342141 0.8891383 -0.090930864 -0.49500078 0.8654859 -0.13922471 -0.49759448 -0.18394092 -0.87766623 -0.7410369 0.10621585 0.5244047 0.37844017 0.024058223 0.78752095 0.3618247 0.80900633 -0.47821358 0.7984024 -0.9058888 -0.8554216 -0.9068364 -0.35494846 -0.84319997 -0.6036904 0.9042927 0.091635376 -0.11074327 -0.025732026 0.6881312 -0.590453 0.29746282 -0.81246763 -0.60796344 -0.68722814 0.85283047 0.08159642 -0.8570137 -0.85794216 0.67010206 -0.41879058 0.44067448 0.8596295 0.43799293 -0.7416377 0.9268815 -0.1297234 0.23661724 0.48412475 0.67597175 0.9079261 -0.52665836 0.9106679 -0.102124974 -0.15129551 -0.10762298 -0.82400084 0.53838515 0.8150033 -0.63103 -0.043885425 0.0879776 0.42031255 0.8096905 -0.8219237 -0.8045856 0.57258767 0.6340139 -0.08463316 -0.7049768 0.8687426 0.46703827 -0.70616174 0.7590643 0.6358374 0.7428731 0.86755216 0.7167369 0.88154966 0.5573708 0.7230853 0.8245705 0.9620808 -0.3535139 0.981297 -0.30206078 0.80207324 0.20489988 0.77773166 0.85460097 -0.8102501 -0.556245 0.8425517 0.26068026 -0.58346665 -0.944479 -0.10337639 0.8890872 0.764282 -0.13533656 -0.90390754 0.3122697 -0.7101809 -0.45474708 -0.6176752 -0.90628725 -0.50176287 -0.6154723'.split(' ')
cv3 = '0.64085674 0.26927942 -0.35969922 -0.91668624 0.40962797 -0.28096685 -0.37260604 -0.19097356 -0.42043567 -0.7046634 0.8543717 0.84445506 0.7112858 -0.17980318 -0.57104194 -0.7828252 -0.18952648 0.37786424 0.41763747 0.15042794 -0.8408891 0.8915771 0.20520243 -0.30805695 0.8418504 -0.21542512 0.14446843 -0.044925258 0.7315006 -0.46648854 -0.48407412 0.9869007 -0.6109047 0.7908162 0.3226099 0.41831988 0.5356137 0.68038195 0.57228434 0.42292637 -0.47028345 -0.3983917 -0.7648041 0.9541754 -0.07896143 0.8307023 -0.84801316 -0.31932926 -0.6468329 0.4374559 -0.9201954 0.89046735 -0.8670378 0.9748081 0.7369414 0.60983074 0.53497297 0.5652022 -0.82059264 0.62499213 -0.45737225 0.86689097 0.33494782 -0.7866151 0.7469607 0.8035226 -0.84124815 -0.4766379 -0.57693505 0.6677401 0.5611316 -0.8471426 -0.8575764 0.848428 -0.7677578 -0.731183 -0.824506 0.56830704 0.61535037 0.41937605 0.84226096 0.48937154 0.98974156 0.7640389 -0.77748835 0.76318145 0.43432862 -0.7995367 0.14052515 0.40406746 -0.4022771 -0.47332895 0.2917288 0.8294605 0.73245037 -0.82690334 -0.6534426 0.8398461 0.34575978 -0.1978634 0.7279341 -0.39665088 0.89516085 0.63248783 0.35222578 0.15885296 -0.8238357 0.7641253 -0.9051316 0.9496112 0.9331714 -0.7851695 -0.7709392 0.93609464 0.5526683 0.53534997 0.5234579 0.6675478 0.2681948 0.2541061 0.7388793 0.37366223 -0.9325308 -0.2543518 -0.8458096 -0.07287607 -0.0042908303 -0.5907017 -0.20485765 0.32882127 -0.34366095 0.94285405 0.20771275 -0.6603 -0.6769309 -0.83092403 0.52944577 -0.6121964 0.42775825 -0.25453222 0.46666673 -0.24190307 0.33473867 -0.7990209 -0.9003285 0.33056217 0.90813637 0.21212144 0.31831992 -0.55864394 0.7702616 -0.801016 0.57846856 0.3021362 0.47443104 -0.28742674 0.2786219 -0.6151235 0.26839387 -0.5758486 -0.09055352 0.47722197 -0.3640077 -0.35710278 0.44879204 -0.40481865 -0.6207359 0.8527162 -0.78899777 -0.8287004 0.22374205 -0.5438854 0.15481032 0.3646948 -0.86172885 -0.9443176 -0.648882 0.40926474 0.39084154 0.436731 -0.9618014 -0.56245774 0.36746174 0.5130806 -0.89604765 0.6157977 0.9028075 -0.5665199 0.92359805 0.7984803 0.028557986 -0.7615072 0.03851212 0.76035357 -0.43177545 0.16700985 0.8802941 -0.27264988 -0.62287664 -0.77644026 -0.8337321 -0.36397523 0.463014 0.7913117 -0.8708223 -0.8656273 -0.23325412 -0.40054289 -0.77160454 0.971806 -0.7415015 -0.32963592 0.35145414 0.07140635 -0.42208865 -0.2984428 0.8115793 0.9232843 0.84992355 -0.97267693 0.27695775 0.66417265 0.22361773 0.536275 -0.45939088 0.49322027 0.4951241 0.12112917 -0.21108285 -0.51712054 0.8945055 0.7445245 0.40139207 -0.7247612 -0.51078886 0.76001203 -0.5814812 -0.7041414 -0.21263388 0.8317987 0.9625052 -0.8732361 0.26013947 0.6588808 0.8083617 -0.93147445 0.46291482 0.58333033 0.9531752 0.21137545 -0.78967726 -0.6603507 -0.7416351 -0.7732295 0.75537044 -0.67774683 -0.6380047 0.8715588 -0.5438829 0.15734836 0.7831819 -0.5859053 -0.3929082 -0.2348326 0.3133612 0.3841539 0.010711519 0.2681548 -0.04691407 -0.6076673 0.32487342 -0.43109918 -0.375454 -0.59027565 -0.49411002 -0.6658265 0.94250464 0.8660768 -0.040376693 0.04800275 0.86965996 0.42506644 -0.031015277 0.62407035 -0.82820624 -0.7116333 0.80354977 -0.846848 -0.3407349 -0.8691918 0.60347897 0.19585572 0.72444224 0.19423631 0.8110346 -0.9585937 0.10314174 -0.9164187 0.7600061 -0.21063545 0.45736766 0.853314 0.17580663 -0.2158648 -0.24826382 -0.6339583 0.18500401 0.77133644 -0.4636149 -0.94424087 0.39726168 0.9141704 -0.07756293 -0.451186 -0.8940801 0.87654185 -0.52640617 0.6831959 0.90839183 0.47692767 -0.9762948 0.90666807 0.8815176 -0.25154012 -0.30598906 0.70620763 0.9220693 0.49997342 0.90325606 -0.56232524 0.04668753 -0.7751556 0.63261545 0.8586767 0.7592151 0.03936059 0.5726447 0.2319431 0.68645203 0.5324965 -0.96415615 -0.8103707 -0.6658952 0.95349187 -0.19094291 -0.64404154 0.864409 0.43530205 -0.9101974 0.39095035 0.66879976 0.3413686 -0.54413843 0.8425757 0.8682939 0.24934267 0.72147727 0.81332004 0.9619962 0.8578371 0.9475158 -0.61144537 0.80278945 0.83866215 -0.90053487 0.83100116 -0.09780285 -0.71306396 0.9026545 0.77029896 0.13212173 -0.9024687 0.08855143 0.7992829 -0.82815117 0.28980917 -0.89632505 -0.48888975 -0.069916815 -0.8851899 0.885072 -0.94252527 -0.8605703 -0.6377934'.split(' ')
cv4 = '0.5734073 -0.61398137 0.42359218 -0.50067383 -0.31744143 0.28601596 0.47893968 0.33539 -0.5896994 -0.31442124 -0.045689236 0.19512056 -0.1066357 0.8522155 0.32170594 0.14846724 -0.23422429 0.25661284 0.35416573 0.30487886 -0.5647065 0.48110425 0.13768789 0.42384893 0.3180273 -0.19174114 0.016844314 0.24200271 -0.40578648 -0.37588412 -0.47123432 0.95795405 -0.24340454 0.019658918 -0.5846294 0.1117049 0.31953198 0.79042125 -0.21061921 -0.012084896 0.027129278 -0.7052179 -0.20803191 0.7851061 0.31973124 0.1471774 -0.40819547 0.59318537 0.15727009 -0.25237408 -0.6992972 0.43370122 -0.08244527 0.84512913 0.515712 0.22130221 0.74716604 0.14718232 -0.24402003 0.9640225 -0.81216246 0.43394202 -0.6068374 0.18780479 -0.33113685 -0.11074837 -0.013787886 -0.32588968 -0.34781218 0.14330208 -0.7163792 -0.20241538 0.016024623 0.17852941 0.16787176 -0.2930765 -0.22273272 0.21848215 -0.13025798 0.017573822 0.33909956 -0.43587756 0.9817923 0.08937031 -0.29877588 0.020677427 0.6210325 -0.11339522 0.25942585 0.047393076 -0.3892953 -0.48249045 0.4958354 0.433446 0.13382526 -0.083155185 0.5155805 0.18507731 -0.32955062 0.13721105 -0.09669563 0.4278052 0.6687054 0.324258 0.2701174 -0.4102205 -0.34516954 0.25953588 -0.57815295 0.5607805 0.7304998 -0.120003134 0.15102322 0.41841003 -0.35558742 0.54676825 -0.5356031 0.062544815 -0.63493127 0.49986917 -0.35558113 0.43655837 -0.7462029 0.015955076 -0.047959752 -0.26736423 0.2152421 0.022326015 0.17483634 -0.6091092 0.47287837 0.58988464 0.75124913 -0.00027429592 -0.06425347 -0.23150644 0.3103322 -0.1225273 -0.29537314 -0.09208961 0.475537 0.30565706 0.1865918 -0.7884743 -0.6348081 -0.39119893 0.7734633 0.31785673 0.43138164 -0.44775012 0.30257583 -0.17981991 0.35829383 -0.3478813 0.36169496 0.09563969 0.08903176 -0.42365015 0.1167032 -0.0013458403 0.043600015 0.61135787 0.24487187 -0.37150684 0.10282005 0.47925118 -0.28120005 0.28022256 -0.5602463 -0.07883548 -0.51710397 0.45030373 -0.44254193 0.45029676 -0.1554276 -0.7565471 -0.47232893 -0.26045159 0.46728134 0.2008805 -0.68873304 0.33236554 0.11021455 -0.11097103 -0.48830575 -0.23327759 0.40618506 -0.2894272 0.6377839 0.107159324 0.2719746 -0.18498518 0.61108345 0.110306665 -0.21365607 0.3146438 0.44851667 0.21839046 -0.92966914 0.24058716 -0.117133714 -0.45769182 0.4783278 -0.2689868 -0.21190658 -0.29863882 0.27768692 -0.31384447 0.24590012 0.80441236 -0.25640967 0.056802146 -0.0026517622 -0.116877586 0.72277826 0.21490476 0.59253436 0.6148474 0.07725818 -0.93769836 0.28325543 -0.45476985 0.06948048 -0.072366044 -0.5666585 0.35773 0.86671764 0.012574082 0.51688415 -0.040327765 0.2513959 -0.007040607 0.20507197 0.009254202 -0.7774562 0.6167948 0.15669964 -0.02202424 0.06257993 0.27003706 0.80015004 -0.3074996 -0.42836958 -0.08555492 -0.044125773 -0.6806055 0.08308834 -0.23438084 0.7401028 0.53559494 0.10700212 0.059824407 -0.3876744 0.14880481 -0.17900927 0.106697865 -0.7762176 0.24354346 -0.4628915 0.05833393 -0.32294232 -0.4407443 -0.5120575 0.7407601 -0.13893285 0.016819492 -0.3664316 -0.113507025 0.14252321 -0.001025565 0.34012184 -0.1303435 0.31043008 0.17623842 0.09344335 -0.08441622 0.74612916 0.37756038 -0.40139654 -0.31370753 0.4406038 -0.022203475 0.24988541 -0.33710033 -0.3272059 -0.25706476 0.11484563 -0.2069051 -0.019017883 -0.32802078 -0.10432807 -0.17643635 0.025212735 0.060520872 0.07528144 -0.83493197 -0.4927969 -0.6458439 -0.28014714 -0.80481476 -0.09536102 0.5235477 -0.31267455 -0.62929875 -0.43372774 -0.59521097 -0.03828396 0.87726724 -0.11581355 -0.7251104 -0.05386279 0.78993034 0.5503899 -0.31414858 -0.69086945 0.2500045 0.37669617 0.3210966 0.35416174 -0.052633807 -0.8817674 0.64228266 0.40293923 -0.2815752 -0.56865925 -0.07452069 0.5057758 -0.51797044 0.30690774 -0.2651909 -0.30247587 0.30812317 -0.18245348 0.36803058 0.20569631 0.21337327 -0.18038207 0.40508336 -0.047849838 -0.09279617 -0.7748252 0.123872496 0.02696335 0.6066234 -0.14778376 -0.5331241 0.17608213 0.7307637 -0.6718548 0.10940439 0.33184877 0.04350014 -0.06357813 0.13079274 0.29119727 0.42775235 -0.4173375 0.48502672 0.8388312 0.22717354 0.7262291 -0.08089016 0.31700137 -0.01670111 -0.28721803 0.38158035 -0.49844062 -0.31065315 0.5223617 -0.07333407 -0.82486665 -0.6448157 -0.0051212097 0.32134926 -0.43730155 -0.5653955 -0.53643477 -0.1269381 -0.057015985 -0.5202465 0.27513033 -0.66790503 -0.3270128 -0.651635'.split(' ')

"""7. Next, we will calculate the cosine similarity of two code vectors."""

# Code adapted from https://www.geeksforgeeks.org/how-to-calculate-cosine-similarity-in-python/
# import required libraries
import numpy as np
from numpy.linalg import norm

# convert the codevectors to numpy arrays
A = np.array(cv1, dtype=float)
B = np.array(cv1, dtype=float)

# compute cosine similarity -- compare the same vector of the same code snippet
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (A-A):", cosine)

# convert the codevectors to numpy arrays
A = np.array(cv1, dtype=float)
B = np.array(cv2, dtype=float)

# compute cosine similarity -- compare between two code snippets
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (A-B):", cosine)

# convert the codevectors to numpy arrays
A = np.array(cv1, dtype=float)
B = np.array(cv3, dtype=float)

# compute cosine similarity -- compare between two code snippets
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV1-CV1):", cosine)

"""8. Write code to create a list of the 4 code vectors and compare all of them."""

# Fill in this part
import numpy as np
from numpy.linalg import norm


A = np.array(cv1, dtype=float)
B = np.array(cv1, dtype=float)


cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV1-CV1):", cosine)


A = np.array(cv1, dtype=float)
B = np.array(cv2, dtype=float)


cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV1-CV2):", cosine)

A = np.array(cv1, dtype=float)
B = np.array(cv3, dtype=float)



cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV1-CV3):", cosine)

A = np.array(cv1, dtype=float)
B = np.array(cv4, dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV1-CV4):", cosine)


A = np.array(cv2 , dtype=float)
B = np.array(cv1 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV2-CV1):", cosine)

A = np.array(cv2 , dtype=float)
B = np.array(cv2 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV2-CV1):", cosine)


A = np.array(cv2 , dtype=float)
B = np.array(cv3 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV2-CV3):", cosine)



A = np.array(cv2, dtype=float)
B = np.array(cv4, dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV2-CV4):", cosine)


A = np.array(cv3 , dtype=float)
B = np.array(cv1 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV3-CV1):", cosine)

A = np.array(cv3 , dtype=float)
B = np.array(cv2 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV3-CV2):", cosine)


A = np.array(cv3 , dtype=float)
B = np.array(cv3 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV3-CV3):", cosine)


A = np.array(cv3, dtype=float)
B = np.array(cv4, dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV3-CV4):", cosine)

A = np.array(cv4 , dtype=float)
B = np.array(cv1 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV4-CV1):", cosine)

A = np.array(cv4 , dtype=float)
B = np.array(cv2 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV4-CV2):", cosine)


A = np.array(cv4 , dtype=float)
B = np.array(cv3 , dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV4-CV3):", cosine)



A = np.array(cv4, dtype=float)
B = np.array(cv4, dtype=float)
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity (CV4-CV4):", cosine)

from google.colab import drive
drive.mount('/content/drive')