import csv
import pandas as pd

qb = pd.DataFrame({'Player':[], 'Team':[], 'AVG':[], 'ST DEV':[]})
rb = pd.DataFrame({'Player':[], 'Team':[], 'AVG':[], 'ST DEV':[]})
wr = pd.DataFrame({'Player':[], 'Team':[], 'AVG':[], 'ST DEV':[]})
te = pd.DataFrame({'Player':[], 'Team':[], 'AVG':[], 'ST DEV':[]})
           
qb_rankings = pd.DataFrame({'Player':[]})
rb_rankings = pd.DataFrame({'Player':[]})
wr_rankings = pd.DataFrame({'Player':[]})
te_rankings = pd.DataFrame({'Player':[]})

pos = ['QB','RB','WR','TE']

#----------------------------------------------- Fantasy Footballers ------------------------------------------------------------#

with open('2022 QB Rankings - Fantasy Footballers Podcast.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:
        i = i + 1
        line = pd.DataFrame({'Player': row['Name'], 'Andy':int(row['Andy']), 'Mike':int(row['Mike']), 'Jason':int(row['Jason'])}, index=[i])
        qb_rankings = pd.concat([qb_rankings,line])

with open('2022 RB Rankings - Fantasy Footballers Podcast.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:
        i = i + 1
        line = pd.DataFrame({'Player': row['Name'], 'Andy':int(row['Andy']), 'Mike':int(row['Mike']), 'Jason':int(row['Jason'])}, index=[i])
        rb_rankings = pd.concat([rb_rankings,line])

with open('2022 WR Rankings - Fantasy Footballers Podcast.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:
        i = i + 1
        line = pd.DataFrame({'Player': row['Name'], 'Andy':int(row['Andy']), 'Mike':int(row['Mike']), 'Jason':int(row['Jason'])},index=[i])
        wr_rankings = pd.concat([wr_rankings,line])

with open('2022 TE Rankings - Fantasy Footballers Podcast.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    i = 0
    for row in reader:
        i = i + 1
        line = pd.DataFrame({'Player': row['Name'], 'Andy':int(row['Andy']), 'Mike':int(row['Mike']), 'Jason':int(row['Jason'])}, index=[i])
        te_rankings = pd.concat([te_rankings,line])

#------------------------------------------------- Jason Boone --------------------------------------------------------------#


with open('score_qb.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    index = len(qb_rankings)
    for row in reader:
        match = False
        for i in range(len(qb_rankings)):
            if row['PLAYER'] in qb_rankings['Player'][i+1] or qb_rankings['Player'][i+1] in row['PLAYER']:
                qb_rankings.loc[(qb_rankings['Player'] == qb_rankings['Player'][i+1],'Boone')] = int(row['ï»¿RK'])
                match = True
        if match == False:
            index = index + 1
            line = pd.DataFrame({'Player': row['PLAYER'], 'Boone':int(row['ï»¿RK'])}, index=[index])
            qb_rankings = pd.concat([qb_rankings,line])

with open('score_rb.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    index = len(rb_rankings)
    for row in reader:
        match = False
        for i in range(len(rb_rankings)):
            if row['PLAYER'] in rb_rankings['Player'][i+1] or rb_rankings['Player'][i+1] in row['PLAYER']:
                rb_rankings.loc[(rb_rankings['Player'] == rb_rankings['Player'][i+1],'Boone')] = int(row['ï»¿RK'])
                match = True
            elif row['PLAYER'] == 'Ken Walker III':
                rb_rankings.loc[(rb_rankings['Player'] == 'Kenneth Walker III','Boone')] = int(row['ï»¿RK'])
                match = True
        if match == False:
            index = index + 1
            line = pd.DataFrame({'Player': row['PLAYER'], 'Boone':int(row['ï»¿RK'])}, index=[index])
            rb_rankings = pd.concat([rb_rankings,line])

with open('score_wr.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    index = len(wr_rankings)
    for row in reader:
        match = False
        for i in range(len(wr_rankings)):
            if row['PLAYER'] in wr_rankings['Player'][i+1] or wr_rankings['Player'][i+1] in row['PLAYER']:
                wr_rankings.loc[(wr_rankings['Player'] == wr_rankings['Player'][i+1],'Boone')] = int(row['ï»¿RK'])
                match = True
            elif row['PLAYER'] == 'Gabriel Davis':
                wr_rankings.loc[(wr_rankings['Player'] == 'Gabe Davis','Boone')] = int(row['ï»¿RK'])
                match = True
        if match == False:
            index = index + 1
            line = pd.DataFrame({'Player': row['PLAYER'], 'Boone':int(row['ï»¿RK'])}, index=[index])
            wr_rankings = pd.concat([wr_rankings,line])

with open('score_te.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    index = len(te_rankings)
    for row in reader:
        match = False
        for i in range(len(te_rankings)):
            if row['PLAYER'] in te_rankings['Player'][i+1] or te_rankings['Player'][i+1] in row['PLAYER']:
                te_rankings.loc[(te_rankings['Player'] == te_rankings['Player'][i+1],'Boone')] = int(row['ï»¿RK'])
                match = True
        if match == False:
            index = index + 1
            line = pd.DataFrame({'Player': row['PLAYER'], 'Boone':int(row['ï»¿RK'])}, index=[index])
            te_rankings = pd.concat([te_rankings,line])

#------------------------------------------------- Underdog --------------------------------------------------------------#

josh = []
josh_ref = {}
hayd = []
hayd_ref = {}

for p in pos:
    josh.clear()
    josh_ref.clear()
    hayd.clear()
    hayd_ref.clear()
    with open('tableDownload.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Pos'] == p:
                if int(row['Josh']) != 225:
                    josh.append(int(row['Josh']))
                    josh_ref[int(row['Josh'])] = row['Name']
                hayd.append(int(row['Hayden']))
                hayd_ref[int(row['Hayden'])] = row['Name']

    if p == 'QB':
        josh.sort()
        for j in range(len(josh)):
            index = len(qb_rankings)
            match = False
            for i in range(len(qb_rankings)):
                if josh_ref[josh[j]] == 'Mitchell Trubisky':
                    qb_rankings.loc[(qb_rankings['Player'] == 'Mitch Trubisky','Josh')] = int(j+1)
                    match = True
                elif josh_ref[josh[j]] in qb_rankings['Player'][i+1] or qb_rankings['Player'][i+1] in josh_ref[josh[j]]:
                    qb_rankings.loc[(qb_rankings['Player'] == qb_rankings['Player'][i+1],'Josh')] = int(j+1)
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': josh_ref[josh[j]], 'Josh':int(j+1)}, index=[index])
                qb_rankings = pd.concat([qb_rankings,line])

        hayd.sort()
        for j in range(len(hayd)):
            index = len(qb_rankings)
            match = False
            for i in range(len(qb_rankings)):
                if hayd_ref[hayd[j]] == 'Mitchell Trubisky':
                    qb_rankings.loc[(qb_rankings['Player'] == 'Mitch Trubisky','Hayden')] = int(j+1)
                    match = True                    
                if hayd_ref[hayd[j]] in qb_rankings['Player'][i+1] or qb_rankings['Player'][i+1] in hayd_ref[hayd[j]]:
                    qb_rankings.loc[(qb_rankings['Player'] == qb_rankings['Player'][i+1],'Hayden')] = int(j+1)
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': hayd_ref[hayd[j]], 'Hayden':int(j+1)}, index=[index])
                qb_rankings = pd.concat([qb_rankings,line])
                
    if p == 'RB':
        josh.sort()
        for j in range(len(josh)):
            index = len(rb_rankings)
            match = False
            for i in range(len(rb_rankings)):
                if josh_ref[josh[j]] in rb_rankings['Player'][i+1] or rb_rankings['Player'][i+1] in josh_ref[josh[j]]:
                    rb_rankings.loc[(rb_rankings['Player'] == rb_rankings['Player'][i+1],'Josh')] = int(j+1)
                    match = True
                elif josh_ref[josh[j]] == 'Ken Walker':
                    rb_rankings.loc[(rb_rankings['Player'] == 'Kenneth Walker III','Josh')] = int(j+1)
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': josh_ref[josh[j]], 'Josh':int(j+1)}, index=[index])
                rb_rankings = pd.concat([rb_rankings,line])

        hayd.sort()
        for j in range(len(hayd)):
            index = len(rb_rankings)
            match = False
            for i in range(len(rb_rankings)):
                if hayd_ref[hayd[j]] in rb_rankings['Player'][i+1] or rb_rankings['Player'][i+1] in hayd_ref[hayd[j]]:
                    rb_rankings.loc[(rb_rankings['Player'] == rb_rankings['Player'][i+1],'Hayden')] = int(j+1)
                    match = True
                elif hayd_ref[hayd[j]] == 'Ken Walker':
                    rb_rankings.loc[(rb_rankings['Player'] == 'Kenneth Walker III','Hayden')] = int(j+1)
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': hayd_ref[hayd[j]], 'Hayden':int(j+1)}, index=[index])
                rb_rankings = pd.concat([rb_rankings,line])
                
    if p == 'WR':
        josh.sort()
        for j in range(len(josh)):
            index = len(wr_rankings)
            match = False
            for i in range(len(wr_rankings)):
                if josh_ref[josh[j]].replace('.','') in wr_rankings['Player'][i+1].replace('.','') or wr_rankings['Player'][i+1].replace('.','') in josh_ref[josh[j]].replace('.',''):
                    wr_rankings.loc[(wr_rankings['Player'] == wr_rankings['Player'][i+1],'Josh')] = int(j+1)
                    match = True
                elif josh_ref[josh[j]] == 'Gabriel Davis':
                    wr_rankings.loc[(wr_rankings['Player'] == 'Gabe Davis','Josh')] = int(j+1)
                    match = True
                elif josh_ref[josh[j]] == 'Robby Anderson':
                    wr_rankings.loc[(wr_rankings['Player'] == 'Robbie Anderson','Josh')] = int(j+1)
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': josh_ref[josh[j]], 'Josh':int(j+1)}, index=[index])
                wr_rankings = pd.concat([wr_rankings,line])

        hayd.sort()
        for j in range(len(hayd)):
            index = len(wr_rankings)
            match = False
            for i in range(len(wr_rankings)):
                if hayd_ref[hayd[j]].replace('.','') in wr_rankings['Player'][i+1].replace('.','') or wr_rankings['Player'][i+1].replace('.','') in hayd_ref[hayd[j]].replace('.',''):
                    wr_rankings.loc[(wr_rankings['Player'] == wr_rankings['Player'][i+1],'Hayden')] = int(j+1)
                    match = True
                elif hayd_ref[hayd[j]] == 'Gabriel Davis':
                    wr_rankings.loc[(wr_rankings['Player'] == 'Gabe Davis','Hayden')] = int(j+1)
                    match = True
                elif hayd_ref[hayd[j]] == 'Robby Anderson':
                    wr_rankings.loc[(wr_rankings['Player'] == 'Robbie Anderson','Hayden')] = int(j+1)
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': hayd_ref[hayd[j]], 'Hayden':int(j+1)}, index=[index])
                wr_rankings = pd.concat([wr_rankings,line])
                
    elif p == 'TE':
        josh.sort()
        for j in range(len(josh)):
            index = len(te_rankings)
            match = False
            for i in range(len(te_rankings)):
                if josh_ref[josh[j]] in te_rankings['Player'][i+1] or te_rankings['Player'][i+1] in josh_ref[josh[j]]:
                    te_rankings.loc[(te_rankings['Player'] == te_rankings['Player'][i+1],'Josh')] = int(j+1)
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': josh_ref[josh[j]], 'Josh':int(j+1)}, index=[index])
                te_rankings = pd.concat([te_rankings,line])

        hayd.sort()
        for j in range(len(hayd)):
            index = len(te_rankings)
            match = False
            for i in range(len(te_rankings)):
                if hayd_ref[hayd[j]] in te_rankings['Player'][i+1] or te_rankings['Player'][i+1] in hayd_ref[hayd[j]]:
                    te_rankings.loc[(te_rankings['Player'] == te_rankings['Player'][i+1],'Hayden')] = int(j+1)
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': hayd_ref[hayd[j]], 'Hayden':int(j+1)}, index=[index])
                te_rankings = pd.concat([te_rankings,line])
                
#------------------------------------------------- Matt Harmon --------------------------------------------------------------#


with open('FantasyPros-QB.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    index = len(qb_rankings)
    for row in reader:
        match = False
        if row['Matt Harmon'] != '':
            for i in range(len(qb_rankings)):
                if row['Player Name'] in qb_rankings['Player'][i+1] or qb_rankings['Player'][i+1] in row['Player Name']:
                    qb_rankings.loc[(qb_rankings['Player'] == qb_rankings['Player'][i+1],'Matt')] = int(row['Matt Harmon'])
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': row['Player Name'], 'Matt':int(row['Matt Harmon'])}, index=[index])
                qb_rankings = pd.concat([qb_rankings,line])

with open('FantasyPros-RB.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    index = len(rb_rankings)
    for row in reader:
        match = False
        if row['Matt Harmon'] != '':
            for i in range(len(rb_rankings)):
                if row['Player Name'] in rb_rankings['Player'][i+1] or rb_rankings['Player'][i+1] in row['Player Name']:
                    rb_rankings.loc[(rb_rankings['Player'] == rb_rankings['Player'][i+1],'Matt')] = int(row['Matt Harmon'])
                    match = True
                elif row['Player Name'] == 'Ken Walker III':
                   rb_rankings.loc[(rb_rankings['Player'] == 'Kenneth Walker III','Matt')] = int(row['Matt Harmon'])
                   match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': row['Player Name'], 'Matt':int(row['Matt Harmon'])}, index=[index])
                rb_rankings = pd.concat([rb_rankings,line])

with open('FantasyPros-WR.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    index = len(wr_rankings)
    for row in reader:
        match = False
        if row['Matt Harmon'] != '':
            for i in range(len(wr_rankings)):
                if row['Player Name'] in wr_rankings['Player'][i+1] or wr_rankings['Player'][i+1] in row['Player Name']:
                    wr_rankings.loc[(wr_rankings['Player'] == wr_rankings['Player'][i+1],'Matt')] = int(row['Matt Harmon'])
                    match = True
                elif row['Player Name'] == 'Gabriel Davis':
                    wr_rankings.loc[(wr_rankings['Player'] == 'Gabe Davis','Matt')] = int(row['Matt Harmon'])
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': row['Player Name'], 'Matt':int(row['Matt Harmon'])}, index=[index])
                wr_rankings = pd.concat([wr_rankings,line])

with open('FantasyPros-TE.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    index = len(te_rankings)
    for row in reader:
        match = False
        if row['Matt Harmon'] != '':
            for i in range(len(te_rankings)):
                if row['Player Name'] in te_rankings['Player'][i+1] or te_rankings['Player'][i+1] in row['Player Name']:
                    te_rankings.loc[(te_rankings['Player'] == te_rankings['Player'][i+1],'Matt')] = int(row['Matt Harmon'])
                    match = True
            if match == False:
                index = index + 1
                line = pd.DataFrame({'Player': row['Player Name'], 'Matt':int(row['Matt Harmon'])}, index=[index])
                te_rankings = pd.concat([te_rankings,line])



#------------------------------------------------- Export to CSV --------------------------------------------------------------#

# Replacing NaN with Max Ranking of Each Ranker
rankers = ['Andy', 'Mike', 'Jason', 'Boone', 'Josh', 'Hayden', 'Matt']
for ranker in rankers:
    qb_rankings[ranker] = qb_rankings[ranker].fillna(max(qb_rankings[ranker]+1))
    rb_rankings[ranker] = rb_rankings[ranker].fillna(max(rb_rankings[ranker]+1))
    wr_rankings[ranker] = wr_rankings[ranker].fillna(max(wr_rankings[ranker]+1))
    te_rankings[ranker] = te_rankings[ranker].fillna(max(te_rankings[ranker]+1))

for i in range(len(qb_rankings)):
    avg = ((qb_rankings.drop(columns=['Player'])).iloc[i]).mean()
    std = ((qb_rankings.drop(columns=['Player'])).iloc[i]).std()  
    line = pd.DataFrame({'Player':qb_rankings.iloc[i]['Player'],'AVG':avg,'ST DEV':std}, index=[0])
    qb = pd.concat([qb,line])

for i in range(len(rb_rankings)):
    avg = ((rb_rankings.drop(columns=['Player'])).iloc[i]).mean()
    std = ((rb_rankings.drop(columns=['Player'])).iloc[i]).std()  
    line = pd.DataFrame({'Player':rb_rankings.iloc[i]['Player'],'AVG':avg,'ST DEV':std}, index=[0])
    rb = pd.concat([rb,line])

for i in range(len(wr_rankings)):
    avg = ((wr_rankings.drop(columns=['Player'])).iloc[i]).mean()
    std = ((wr_rankings.drop(columns=['Player'])).iloc[i]).std()  
    line = pd.DataFrame({'Player':wr_rankings.iloc[i]['Player'],'AVG':avg,'ST DEV':std}, index=[0])
    wr = pd.concat([wr,line])

for i in range(len(te_rankings)):
    avg = ((te_rankings.drop(columns=['Player'])).iloc[i]).mean()
    std = ((te_rankings.drop(columns=['Player'])).iloc[i]).std()  
    line = pd.DataFrame({'Player':te_rankings.iloc[i]['Player'],'AVG':avg,'ST DEV':std}, index=[0])
    te = pd.concat([te,line])
    
qb.to_csv('rankings_qb.csv',index=False)
rb.to_csv('rankings_rb.csv',index=False)
wr.to_csv('rankings_wr.csv',index=False)
te.to_csv('rankings_te.csv',index=False)







    
