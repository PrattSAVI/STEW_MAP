#%% Import data and Dependencies
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
pd.options.display.max_columns = None
import seaborn as sns

df = gpd.read_file( r"C:\Users\csucuogl\Documents\GitHub\STEW_MAP\Stew_Map_LA\Turfs.shp")
df.crs = {'init' :'epsg:4326'}

df.head(5)

#%% MapYN
indi = 'MapYN'
print(df[indi].unique())

replace = [(1,"Y"),(2,"N")]
for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)
# %% OrgType

replace = [
(1, '501(c)(3) (or has applied)'),
(2, "501 (c)(4) (or has applied)" ),
(3, "Community group/organization without 501(c)(3) or 501(c)(4) status (for example, a community garden group or block club)"),
(4, "Local government agency"),
(5, "State government agency"),
(6, "Federal government agency"),
(7, "Public administration district"),
(8, "Private firm, for-profit business"),
(9, "Other – please specify:")]

indi = 'OrgType'
print(df[indi].unique())

for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)

# %% Easy Division 

def divider(strs):
    a = []
    for i in strs.split("\n"):
        if len(i)>1:
            a.append( (float(i.split(':')[0]),i.split(':')[1]) )
    return a  

#%% Prim Focus

strs = '''
1: Public health (including mental health, crisis intervention, health care)
2: Education
3: Transportation
4: Housing and shelter
5: Community improvement and capacity building
6: Environment (including gardening, forestry, ecological restoration, water and air protection, and land management)
7: Toxics/pollution related
8: Animal related
9: Human services (including day care, family services)
10: Youth 	
11: Economic development
12: Employment, job related
13: Legal services, civil rights
14: Arts, culture, creative practices
15: Recreation and sports (including birding and fishing)
16: Crime, criminal justice
17: International, foreign affairs, and national security
18: Research in science and/or technology
19: Faith-based activities
20: Power/electricity generation
21: Energy Efficiency
22: Private grantmaking foundation
23: Seniors
24: Food
25: Other'''

replace = divider(strs)

indi = 'PrimFocus'
print(df[indi].unique())

for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)

#%% Replace Columns Name

df.columns = df.columns.str.replace("PrimFocus", "OrgFocus")
df.columns = df.columns.str.replace('PrmFc_Txt', "OrgFoc_Ot")
df.columns = df.columns.str.replace('Fund_Prefe', "Fnd_Prefer")
df.columns = df.columns.str.replace('Primary_Fu', 'Fnd_Prim')
df.columns = df.columns.str.replace('Funding_So', 'Fnd_Ot')

df.head(5)

# %% Pct Stew

df.columns[ df.columns.str.contains("Pct")]

strs = '''
1: 0-19%
2: 20-39%
3: 40-59%
4: 60-79%
5: 80-100%
'''

replace = divider(strs)

indi = 'PctStew'
print(df[indi].unique())

for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)


# %%

df.columns[ df.columns.str.contains("GIS")]

strs = '''
1: Yes
2: No
'''

replace = divider(strs)

indi = 'GISYN'
print(df[indi].unique())

for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)


# %%

df.columns[ df.columns.str.contains("PriLandOwn")]

strs = '''
1: Federal government
2: State government
3: County government
4: City/Local government
5: Other government (e.g. Port Authority)
6: Individual
7: Corporation (including joint ventures, real estate investment groups)
8: Nonprofit
9: Don't know
10: Other:
'''

replace = divider(strs)

indi = 'PriLandOwn'
print(df[indi].unique())

for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)


# %%

df.columns[ df.columns.str.contains("PriLandOwn")]

strs = '''
1: Yes, we own the entire property
2: Yes, we own a part of the property
3: Yes, we have a legal interest or a conservation easement on the property
4: No, we do not own any part of the property

'''

replace = divider(strs)

indi = 'Org_Own_St'
print(df[indi].unique())

for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)
# %% Disclose Funding Amount YN

df.columns[ df.columns.str.contains("Fnd_Prefer")]

strs = '''
1: (Agreed to enter budget)
2: Prefer not to answer
'''

replace = divider(strs)

indi = 'Fnd_Prefer'
print(df[indi].unique())

for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)

# %%

df.columns[ df.columns.str.contains("Fnd_Prim")]

strs = '''
1: Government agencies
2: Foundations
3: Endowment		
4: Individual memberships
5: Fees/program income
6: Corporate giving/sponsorship
7: Other
'''

replace = divider(strs)

indi = 'Fnd_Prim'
print(df[indi].unique())

for i,r in replace:
    df[indi] = df[indi].replace( i,r )

df.sample(5)
# %%

df.columns = df.columns.str.replace('OF_Youth',"Temp")
df.columns = df.columns.str.replace('OrgFnOther', 'OF_Youth')
df.columns = df.columns.str.replace('Temp', 'OrgFn_Ot')

df.head(5)

# %%

df[ ~df['OrgFn_Ot'].isnull() ][['OrgFn_Ot',"OrgFoc_Ot"]]


# %%

df.to_file(r"C:\Users\csucuogl\Documents\GitHub\STEW_MAP\Stew_Map_LA\210324_Turfs.shp")
# %%
