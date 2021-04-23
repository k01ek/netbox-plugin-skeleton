# NetBox Plugin Skeleton
The skeleton for [Netbox](https://github.com/netbox-community/netbox) plugin.  
Basically, it's a Django app skeleton, which contains all necessary (and unnecessary) files for building a new plugin.

## Instructions
### Donwload repositioriy
You can get this skeleton in two ways:
1. Create your own GitHub repository using that one as a template [HowTo](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)
2. Clone this repo or download it as an archive
### Replace the name of the plugin in files and filenames with your new name
Use repren script for replacing name. Set the new name of your plugin as an argument to the script.    
Example:
```
python3 develop/repren.py my_new_plugin 
Found 29 files in: .
- modify: ./Makefile: 3 matches
- modify: ./MANIFEST.in: 1 matches
- modify: ./setup.py: 1 matches
- modify: ./README.me: 1 matches
- modify: ./develop/configuration.py: 1 matches
- modify: ./develop/docker-compose.yml: 4 matches
- rename: ./netbox_newplugin/signals.py -> ./my_new_plugin/signals.py
- rename: ./netbox_newplugin/version.py -> ./my_new_plugin/version.py
- rename: ./netbox_newplugin/tamplate_content.py -> ./my_new_plugin/tamplate_content.py
- rename: ./netbox_newplugin/models.py -> ./my_new_plugin/models.py
- modify: ./netbox_newplugin/__init__.py: 1 matches
- rename: ./netbox_newplugin/__init__.py -> ./my_new_plugin/__init__.py
- rename: ./netbox_newplugin/forms.py -> ./my_new_plugin/forms.py
- rename: ./netbox_newplugin/admin.py -> ./my_new_plugin/admin.py
- rename: ./netbox_newplugin/tables.py -> ./my_new_plugin/tables.py
- modify: ./netbox_newplugin/navigation.py: 1 matches
- rename: ./netbox_newplugin/navigation.py -> ./my_new_plugin/navigation.py
- rename: ./netbox_newplugin/urls.py -> ./my_new_plugin/urls.py
- rename: ./netbox_newplugin/filters.py -> ./my_new_plugin/filters.py
- rename: ./netbox_newplugin/middleware.py -> ./my_new_plugin/middleware.py
- rename: ./netbox_newplugin/views.py -> ./my_new_plugin/views.py
- modify: ./netbox_newplugin/api/serializers.py: 1 matches
- rename: ./netbox_newplugin/api/serializers.py -> ./my_new_plugin/api/serializers.py
- rename: ./netbox_newplugin/api/__init__.py -> ./my_new_plugin/api/__init__.py
- rename: ./netbox_newplugin/api/urls.py -> ./my_new_plugin/api/urls.py
- modify: ./netbox_newplugin/api/views.py: 1 matches
- rename: ./netbox_newplugin/api/views.py -> ./my_new_plugin/api/views.py
- rename: ./netbox_newplugin/templates/netbox_newplugin/example -> ./my_new_plugin/templates/my_new_plugin/example
Found 29 files in: .
- modify: ./README.me: 1 matches
- modify: ./my_new_plugin/__init__.py: 2 matches
```
### Fix LICENSE file if you want
### Fill in other information about the plugin
Set name, url, author, description, etc in `README`, `setup.py`, and `__init__.py`
### Commit changes
If the repo was cloned, just remove .git folder 
```
rm -rf .git
```
and set your own repo like this
```
git init
git add .
git commit -m 'init'
```
### Helpfulness
Useful tools for developing the plugin you can find in the develop folder of this repo.
Use Makefile to run a new development environment with docker in 3 commands. (docker and docker-compose required).   

0. Set `PYTHON_VER` and `NETBOX_VER` in Makefile or environment
```
PYTHON_VER?=3.7
NETBOX_VER?=v2.10.3
```
1. Build netbox container
```
make cbuild
docker-compose -f ./develop/docker-compose.yml \
		-p my_new_plugin build \
		--build-arg netbox_ver=v2.10.3 \
		--build-arg python_ver=3.7
postgres uses an image, skipping
redis uses an image, skipping
Building netbox
[+] Building 1.7s (15/15) FINISHED                                                                                                              
...
Successfully built ec6e8aabbaddb7c4386aef8f779d9ae7e8562f521e9041b7c20a3233f4c3a6d9
Building worker
[+] Building 0.2s (15/15) FINISHED                                                                                                              
...
Successfully built ec6e8aabbaddb7c4386aef8f779d9ae7e8562f521e9041b7c20a3233f4c3a6d9
```
2. Run netbox container
```
make debug
```
3. Add django superuser
```
make adduser
docker-compose -f ./develop/docker-compose.yml -p my_new_plugin run netbox python manage.py createsuperuser
Creating my_new_plugin_netbox_run ... done
Username (leave blank to use 'root'): admin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```

### Notes
If you got the error with git after change plugin name like this:  
`fatal: unknown index entry format 0x196e0000`  
use following commands to fix it
```
rm -f .git/index
git reset
```
