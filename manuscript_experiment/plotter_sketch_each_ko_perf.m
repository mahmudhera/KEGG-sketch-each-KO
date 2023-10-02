
memories = [16.7821259765625 32.90168359375 48.365880859375 64.68860058593751 80.5376474609375
12.985487304687501 29.6420615234375 44.3457734375 57.6894658203125 67.2266748046875
11.549642578124999 26.8338740234375 41.062966796874996 52.589518554687494 64.2343212890625];

meories_error = [0.6655918573723082 0.18063641544159276 1.3523711538784613 0.3645597571183638 0.3998017528270802
1.241129518195058 2.1306704943053445 2.771234240037759 2.204723801682021 1.300557503090423
1.6257741669687804 1.724752229173223 1.6481250756331345 1.7108956592815001 2.4085038556186276];

category_names = {'2M', '4M', '6M', '8M', '10M'};

Y = memories';
Y_er = meories_error';
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

set(gcf, 'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on;
grid on;
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none','LineWidth', 0.9);%Adding the errorbars
hold off
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=7', 'sourmash, k=11', 'sourmash, k=15', 'Location', 'Best');

title('Memory required to idnetify KOs by various approaches', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average memory used (GB)', 'FontSize', 10);

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'large_MGs_memory.pdf', '-dpdf', '-bestfit');

%%

times = [3.5993085382663232 3.8262561770789496 3.8418426701995676 4.05441311016134 3.95584178246067
2.4397964634832663 2.6782403267595845 2.8162918271475537 2.911012680955343 2.981098333177502
2.4073683879566192 2.6536512990334544 2.7920375409043032 2.885635057490548 2.960218350367012];

times_error = [0.1242151715460859 0.1342966963402152 0.17215207697473198 0.008907589798558012 0.14883567594966893
0.008712704651757925 0.004507182739907113 0.005410083590945953 0.009132579495130577 0.014616710598757214
0.008150532475872 0.0059428637930367696 0.0054949526674289255 0.006635973444802325 0.012926315922547824];

category_names = {'2M', '4M', '6M', '8M', '10M'};

Y = times';
Y_er = times_error';
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

set(gcf, 'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on;
grid on;
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none','LineWidth', 0.9);%Adding the errorbars
hold off
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=11', 'sourmash, k=15', 'Location', 'Best');

title('Running time for identifying KOs by various approaches', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average running time (seconds)', 'FontSize', 10);
yticklabels({'10^0', '', '10^1', '', '10^2', '', '10^3', '', '10^4'})

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'large_MGs_runtime.pdf', '-dpdf', '-bestfit');

%%

f1s = [0.8847301712742383 0.8880619749489485 0.8896259142881779 0.8908775978321698 0.8905484084161788
0.8432734149969336 0.8684417027831037 0.8887103544491444 0.8952142981548598 0.8990073275891041
0.8363578700417402 0.8720934905977167 0.8891791996209022 0.8916305708625766 0.9000452651024572 ];

f1s_error = [0.005273069453116441 0.005443651305338725 0.006142412153790997 0.006079503730739759 0.006966635807099837
0.0038639536500277806 0.0025908049368146965 0.0031997973665810675 0.004144013850516707 0.0029998614429398445
0.0037075740342993333 0.0017204188022984282 0.0017140448805185904 0.0026591063615494237 0.001627776636061025 ];

category_names = {'2M', '4M', '6M', '8M', '10M'};

Y = f1s'*100;
Y_er = f1s_error'*100;
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

set(gcf, 'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on;
grid on;
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none', 'LineWidth', 0.9);%Adding the errorbars
hold off
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=11', 'sourmash, k=15', 'Location', 'west');
title('F1 scores in identifying KOs by various approaches', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average F1 score', 'FontSize', 10);

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'large_MGs_F1.pdf', '-dpdf', '-bestfit');

%%

recalls = [0.8691224800254214 0.8714762695154663 0.873877180607319 0.8753224108870136 0.8751047462412679
0.793539213187585 0.9121977865442167 0.899407507417639 0.8866392604270988 0.91049247237624
0.7874706242388564 0.9037782212891011 0.8895108869425797 0.9040660521954076 0.9040838972720966 ];

recalls_error = [0.011528227853333364 0.01019371743486841 0.01029700585794212 0.01076347223974885 0.010755326320193841
0.006535672467911275 0.0030578463378402314 0.006332341111502415 0.012983668041781337 0.0062331479948933175
0.04071468008873657 0.0045798766548551745 0.002552073337471258 0.02703456743527988 0.0024697565980176814];

category_names = {'2M', '4M', '6M', '8M', '10M'};

Y = recalls'*100;
Y_er = recalls_error'*100;
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

set(gcf,'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on
grid on
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none', 'LineWidth', 0.9);%Adding the errorbars
hold off
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=11', 'sourmash, k=15', 'Location', 'Best');
title('Recalls (completeness scores) in identifying KOs by various approaches', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average recall (completeness)', 'FontSize', 10);

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'large_MGs_recall.pdf', '-dpdf', '-bestfit');

%%

precisions = [0.9011350055893483 0.9054644057096011 0.9061343942328219 0.9071795220328471 0.9067190486855352
0.8996985661424658 0.8287075577267649 0.8783021392064526 0.9045022083606827 0.8878516411869238
0.8965895227312869 0.8425830140345258 0.8888569787220236 0.8813594438026293 0.896050692325673];

precisions_error = [0.010674823670584244 0.010133839599430193 0.011211439705071718 0.010764946317963013 0.011374969061685676
0.003108252546158766 0.004257747239165635 0.0038705009494054868 0.018369574193220283 0.0044307572388060535
0.04431682251400676 0.0034439108912748084 0.002752404068744034 0.030872057487310513 0.002565605671598089];

%category_names = {'1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M', '9M', '10M'};
category_names = {'2M', '4M', '6M', '8M', '10M'};

Y = precisions'*100;
Y_er = precisions_error'*100;
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

set(gcf, 'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on;
grid on;
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none', 'LineWidth', 0.9);%Adding the errorbars
hold off;
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=11', 'sourmash, k=15', 'Location', 'Best');
title('Precisions (purity scores) in identifying KOs by various tools', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average precision (purity) in identifying KOs', 'FontSize', 10);

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'large_MGs_precision.pdf', '-dpdf', '-bestfit');
%%

times = [1.9281081992747524 2.005597142347061 2.0142350736943704 2.157398243822439 2.130168818408767
1.0134620812097483 1.0084988314290126 0.9730169353069114 1.014872874507723 1.0297368830166767 
0.9810852033310182 1.0115995397738162 0.9697642196628193 1.0133565378510754 1.020356512236863
2.810238570195133 2.8843570827217566 3.1011531328342308 3.270920925508024 3.296401143614665 ];

times_error = [0.0694046620324682 0.05345969811128431 0.05826469016163988 0.0734978495012771 0.07584186716120868
0.06403489674112783 0.05836348009931109 0.08070288794209939 0.05167967117276125 0.020746026668425795 
0.06530733185603799 0.044328840335494946 0.06003893053356753 0.07210225436396077 0.03725488156371673
0.08851132296414017 0.11010172688151021 0.07197504831376413 0.12432980525825636 0.1480338660339257 ];

category_names = { '10K' '20K' '30K' '40K' '50K'};

Y = times';
Y_er = times_error';
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

set(gcf, 'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on;
grid on;
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none','LineWidth', 0.9);%Adding the errorbars
hold off
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=11', 'sourmash, k=15', 'KofamScan', 'Location', 'Best');

title('Running time for identifying KOs by various approaches', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average running time (seconds)', 'FontSize', 10);

yticklabels({'10^0', '', '10^1', '', '10^2', '', '10^3'});

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'small_MGs_runtime.pdf', '-dpdf', '-bestfit');

%%

f1s = [0.7036103948576978 0.7750977946410245 0.8065375467856569 0.8272762809240822 0.794818578441277
0.1997364059578411 0.25238766057469414 0.2896984005724397 0.31939008790471546 0.3937483813999844
0.18358623382030134 0.2268316072312288 0.2637787404262069 0.29542851452401153 0.3672372021854116
0.014290895683581661 0.02121512500710925 0.025042427877745126 0.02834185370620713 0.03193758720333386 ];

f1s_error = [0.019247904066787138 0.014640266526369905 0.013559560234084255 0.012015689581233762 0.007837503989119202
0.017668189310268933 0.017980598490932732 0.012186090592529222 0.010234158477759051 0.009649142750823812
0.015511026660934357 0.01219650384076225 0.008804692325919967 0.010042667254320263 0.011989286884239198
0.0032262319756699814 0.0024126439802736074 0.0030083131752483535 0.0025064640304727093 0.0024522811649590097 ];

category_names = { '10K' '20K' '30K' '40K' '50K'};

Y = f1s'*100;
Y_er = f1s_error'*100;
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

set(gcf, 'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on;
grid on;
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none', 'LineWidth', 0.9);%Adding the errorbars
hold off
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=11', 'sourmash, k=15', 'KofamScan', 'Location', 'west');
title('F1 scores in identifying KOs by various approaches', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average F1 score', 'FontSize', 10);

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'small_MGs_F1.pdf', '-dpdf', '-bestfit');

%%

recalls = [0.669718077301596 0.7342472633580487 0.7647353678649813 0.7873912560463041 0.76482316780426
0.11490781795552671 0.14796113780781434 0.17262019784479093 0.19311147917856647 0.25443297092324124
0.10436799162005853 0.13061002145703607 0.15452799712562032 0.17588597544196743 0.23255180689589147
0.008469368077915243 0.01227839457834251 0.014391208473335002 0.016260793171863873 0.019007919922406517];

recalls_error = [0.030033170734385214 0.026906765225247587 0.025480281029699542 0.024494043055033964 0.013640216437979686
0.010902120379453317 0.011871390904064982 0.008315976013053365 0.007309673849755055 0.007952213489643246
0.009692220881452704 0.007879202728263432 0.005951260319952497 0.007101944558611059 0.009505979578359684
0.0019522401706521893 0.0013877906382439274 0.0017545639874055503 0.0014934348329733109 0.0015221929353096408 ];

category_names = { '10K' '20K' '30K' '40K' '50K'};

Y = recalls'*100;
Y_er = recalls_error'*100;
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

x0 = 10;
y0 = 10;
width = 1200;
height = 400;
set(gcf,'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on
grid on
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none', 'LineWidth', 0.9);%Adding the errorbars
hold off
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=11', 'sourmash, k=15', 'KofamScan', 'Location', 'Best');
title('Recalls (completeness scores) in identifying KOs by various approaches', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average recall (completeness)', 'FontSize', 10);

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'small_MGs_recall.pdf', '-dpdf', '-bestfit');

%%

precisions = [0.7417879179060136 0.8214159839308645 0.8537830842021454 0.8720237698407498 0.8274949154943675
0.765660239040467 0.861150406807198 0.901623599749588 0.9237961719654179 0.8708848310725305
0.7661098374289097 0.8636211918136146 0.9013184660368484 0.9235935963572557 0.8737953342700923
0.04585063519560459 0.0781185741415548 0.0966555408860019 0.11059268918501355 0.1000815732242107 ];

precisions_error = [0.0111497501156853 0.005830455216506708 0.007147569704363173 0.0069073344555911215 0.009772115402133309
0.03952365812955189 0.018482604409739496 0.013272566961019232 0.008786229050851989 0.005751064411028851
0.028336072519777787 0.011606443196017476 0.008109538634984974 0.00956821836612765 0.00776196777357763
0.009466610564050564 0.009843155719145362 0.01141928594065853 0.008797403105098753 0.007078576384421362 ];

category_names = { '10K' '20K' '30K' '40K' '50K'};

Y = precisions'*100;
Y_er = precisions_error'*100;
cat_label = categorical(category_names); %The Group Label
cat_label = reordercats(cat_label,category_names);%To Preserve Label Order
b = bar(Y,'grouped', 'BarWidth', 1.0);

set(gcf, 'units', 'inch', 'position',[0, 0, 8.5, 4]);
set(gca, 'FontName', 'Arial');
hold on;
grid on;
% Calculate the number of groups and number of bars in each group
[ngroups,nbars] = size(Y);
% Get the x coordinate of the bars
x = nan(nbars, ngroups);
for i = 1:nbars
    x(i,:) = b(i).XEndPoints;
end
errorbar(x',Y,Y_er,'k','linestyle','none', 'LineWidth', 0.9);%Adding the errorbars
hold off;
set(gca,'xticklabel',cat_label);
legend('Diamond', 'sourmash, k=11', 'sourmash, k=15', 'KofamScan', 'Location', 'Best');
title('Precisions (purity scores) in identifying KOs by various tools', 'FontSize', 11);
xlabel('Number of reads in simulated metagenome', 'FontSize', 10);
ylabel('Average precision (purity) in identifying KOs', 'FontSize', 10);

set(gcf, 'PaperUnits', 'inches');
set(gcf, 'PaperSize', [8.5 4]);
print(gcf, 'small_MGs_precision.pdf', '-dpdf', '-bestfit');
