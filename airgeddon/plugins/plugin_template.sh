#!/usr/bin/env bash

#Global shellcheck disabled warnings
#shellcheck disable=SC2034,SC2154

#Start modifying below this line. You can safely remove comments but be pretty sure to know what you are doing!

###### QUICK SUMMARY ######

#How it works? This system allows to modify functionality of airgeddon to create a custom behavior based on a system of prehooking, overriding and posthooking functions
#This can be done without any modification in the main script. All you need is to do modifications at plugins directory
#Ready? Three simple steps!
#1. Set some generic vars and some requirements vars to set some validations
#2. Check airgeddon main script code and choose a function to work with (you need to be sure which function is doing the part you want to modify. Debug mode can help here)
#3. Code your own stuff. You can set as much functions to prehook, override or posthook as you want. You can also create your own functions to be called from a hooked function

#Bear in mind that this plugin template is ignored by airgeddon and is not executed because of its special filename which is an exception for the system
#To use this template just rename the file to any other filename keeping .sh extension
#Example: my_super_pr0_plugin.sh
#If you have any doubt about plugins development check our Wiki: https://github.com/v1s1t0r1sh3r3/airgeddon/wiki/Plugins%20Development

###### GENERIC PLUGIN VARS ######

plugin_name="Set your plugin name here"
plugin_description="Set a short description of your plugin"
plugin_author="Set your nick/name here"

#Enabled 1 / Disabled 0 - Set this plugin as enabled - Default value 1
plugin_enabled=1

###### PLUGIN REQUIREMENTS ######

#Set airgeddon versions to apply this plugin (leave blank to set no limits, minimum version recommended is 10.0 on which plugins feature was added)
plugin_minimum_ag_affected_version="10.0"
plugin_maximum_ag_affected_version=""

#Set only one element in the array "*" to affect all distros, otherwise add them one by one with the name which airgeddon uses for that distro (examples "BlackArch", "Parrot", "Kali")
plugin_distros_supported=("*")

###### CUSTOM FUNCTIONS ######

#Just create here new custom functions if they are needed
#They can be called from the plugin itself. They are different than the "hooked" functions (explained on the next section)

###### FUNCTION HOOKING: OVERRIDE ######

#To override airgeddon functions, just define them following this nomenclature name: <plugin_short_name>_override_<function_name>
#plugin_short_name: This is the name of the plugin filename without extension (.sh)
#function_name: This is the name of the airgeddon function you want to rewrite with new content

#Overridden function example
#This will replace an existing function in main airgeddon script to change its behavior in order to execute this content instead of the original
#In this template the existing function is called "somefunction" but of course this is not existing in airgeddon. You should replace "somefunction" with the real name of the function you want to override
#Remember also to modify the starting part of the function "plugin_template" to set your plugin short name (filename without .sh) "my_super_pr0_plugin" if you renamed this template file to my_super_pr0_plugin.sh
#Example name: function my_super_pr0_plugin_override_set_chipset() { <- this will override the content of the chosen function
function plugin_template_override_somefunction() {

	echo "Here comes my custom code content which will replace the original source code of the overridden function"
}

###### FUNCTION HOOKING: PREHOOK ######

#To prehook airgeddon functions, just define them following this nomenclature name: <plugin_short_name>_prehook_<function_name>
#plugin_short_name: This is the name of the plugin filename without extension (.sh)
#function_name: This is the name of the airgeddon function where you want to launch your stuff before

#Prehook function example
#This will execute this content before the chosen function
#In this template the existing function is called "somefunction" but of course this is not existing in airgeddon. You should replace "somefunction" with the real name of the function you want to prehook
#Remember also to modify the starting part of the function "plugin_template" to set your plugin short name (filename without .sh) "my_super_pr0_plugin" if you renamed this template file to my_super_pr0_plugin.sh
#Example name: function my_super_pr0_plugin_prehook_clean_tmpfiles() { <- this will execute the custom code just before executing the content of the chosen function
function plugin_template_prehook_somefunction() {

	echo "Here comes my custom code which will be executed just before starting to execute the content of the chosen function"
}

###### FUNCTION HOOKING: POSTHOOK ######

#To posthook airgeddon functions, just define them following this nomenclature name: <plugin_short_name>_posthook_<function_name>
#plugin_short_name: This is the name of the plugin filename without extension (.sh)
#function_name: This is the name of the airgeddon function where you want to launch your stuff after

#Posthook function example
#This will execute this content just after the chosen function
#In this template the existing function is called "somefunction" but of course this is not existing in airgeddon. You should replace "somefunction" with the real name of the function you want to posthook
#Remember also to modify the starting part of the function "plugin_template" to set your plugin short name (filename without .sh) "my_super_pr0_plugin" if you renamed this template file to my_super_pr0_plugin.sh
#Example name: function my_super_pr0_plugin_posthook_clean_tmpfiles() { <- this will execute the custom code just after executing the content of the chosen function
function plugin_template_posthook_somefunction() {

	echo "Here comes my custom code which will be executed just after finish executing the content of the chosen function"
}

#Important notes about returning codes on posthooking
#If the function you are posthooking has a returning code, that value is available on the posthook function as ${1}.
#The return done on the posthook function will be the final return value for the function overriding the original one.
#So if you are posthooking a function with return codes you must do mandatorily a return statement on the posthook function.
