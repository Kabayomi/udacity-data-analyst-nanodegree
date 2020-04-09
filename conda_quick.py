#The following codes are to be run from the terminal or anaconda prompt

#list all environments
conda env list

#add envionment
conda -n env_name python=3 numpy pandas matplotlib 

#remove environment
conda env remove -n env_name 

#Copy your environment configuration to yaml file
conda env export > environment.yaml

#copy environment configuration to .txt file with pip freeze
pip freeze > requirements.txt

#create new environment from yaml file
conda env create -f environment.yaml
