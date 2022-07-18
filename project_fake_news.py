class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def wordopt(text):
    import re
    import string
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

def load_function():
  ''' This function loads the saved joblibs model from the models directory
      and returns them as an output.
  '''
  from joblib import load
  loaded_LR=load(filename="./models/LinearRegression.joblib")
  loaded_DT=load(filename="./models/DecisionTreeClassifier.joblib")
  loaded_GBC=load(filename="./models/GradientBoostingClassifier.joblib")
  loaded_RFC=load(filename="./models/RandomForestClassifier.joblib")
  return loaded_LR,loaded_DT,loaded_GBC,loaded_RFC

def output_lable_colored(n):
    if n == 0:
        return color.BOLD+color.RED+"Fake News"+color.END
    elif n == 1:
        return color.BOLD+color.GREEN+"Real News"+color.END

def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Real News"

def news_manager(news):
    '''Manages the news by converting the long single-line news string
    into multi-line news string'''
    if (len(news)>1355):
        news=news[:1355]+"......"
    s=news
    i=60
    while i<len(s):
        if s[i]==" ":
            s= s[:i]+"\n"+s[i+1:]
            i=i+60
        else:
            i=i+1
    return(s)