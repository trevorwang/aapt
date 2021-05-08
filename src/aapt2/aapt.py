#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
File: aapt2/aapt.py
Project: aapt
Description:
Created By: Tao.Hu 2019-07-08
-----
Last Modified: 2020-10-14 02:03:42 pm
Modified By: Trevor Wang
-----
'''

import os
import re
import stat
import subprocess
import platform
import io
import zipfile
import pathlib


def aapt(args='--help'):
    try:
        # Darwin: macOS Linux Windows
        system_name = platform.system()
        if (system_name != 'Darwin' and system_name != 'Linux' and system_name != 'Windows'):
            raise TypeError(
                'unknown system type, only support Darwin、Linux、Windows')

        aapt_path = os.path.join(os.path.dirname(
            __file__), 'bin', system_name, 'aapt_64')
        if system_name == 'Windows':
            aapt_path += '.exe'

        if (system_name != 'Windows' and os.access(aapt_path, os.X_OK) is not True):
            os.chmod(aapt_path, stat.S_IRWXU)

        out = subprocess.getoutput(aapt_path + ' ' + args)
        return out
    except Exception as e:
        print('aapt error:', e)
        raise e


def ls(file_path):
    return aapt('l ' + file_path)


def dump(file_path, values):
    return aapt('d ' + values + ' ' + file_path)


def packagecmd(file_path, command):
    return aapt('p ' + command + ' ' + file_path)


def remove(file_path, files):
    return aapt('r ' + file_path + ' ' + files)


def add(file_path, files):
    return aapt('a ' + file_path + ' ' + files)


def crunch(resource, output_folder):
    return aapt('c -S ' + resource + ' -C ' + output_folder)


def single_crunch(input_file, output_file):
    return aapt('s -i ' + input_file + ' -o ' + output_file)


def version():
    return aapt('v')


def get_apk_info(file_path):
    try:
        stdout = dump(file_path, 'badging')
        match = re.compile(
            "package: name='(\\S+)' versionCode='(\\d+)' versionName='(\\S+)'").match(stdout)
        if not match:
            raise Exception("can't get packageinfo")
        package_name = match.group(1)
        version_code = match.group(2)
        version_name = match.group(3)
        match = re.compile(
            "application: label='([\u4e00-\u9fa5_a-zA-Z0-9-\\S\s]+)'").search(stdout)
        if not match:
            raise Exception("can't get application label")
        app_name = match.group(1)
        icon_path = get_icon_path(stdout)
        permissions = get_permissions(stdout)

        launchable_activity = get_launchable_activity(stdout)
        return {
            'package_name': package_name,
            'version_code': version_code,
            'version_name': version_name,
            'app_name': app_name,
            'icon_path': icon_path,
            'permissions': permissions,
            'launchable_activity': launchable_activity
        }
    except Exception as e:
        raise e


def get_icon_path(stdout):
    match = re.compile(
        "application: label='([\u4e00-\u9fa5_a-zA-Z0-9-\\S\s]+)' icon='(\\S+)'").search(stdout)
    icon_path = (match and match.group(2)) or None
    return icon_path


def get_permissions(stdout):
    permissions = []
    matches = re.compile(
        "uses-permission: name='([\w\.-]+)'").findall(stdout)
    for m in matches:
        permissions.append(m)
    return permissions


def get_launchable_activity(stdout):
    match = re.compile(
        "launchable-activity: name='([\w\.-]+)'").search(stdout)
    launchable_activity = (match and match.group(1)) or None
    return launchable_activity


def get_apk_and_icon(file_path):
    try:
        apkInfo = get_apk_info(file_path)
        if (apkInfo['icon_path']):
            apkInfo['icon_suffix'] = apkInfo['icon_path'].split(".")[-1]
            apkInfo['icon_byte_value'] = extract_file_from_apk(file_path,
                                                               apkInfo['icon_path'])['byte_value']
        else:
            apkInfo['icon_suffix'] = None
            apkInfo['icon_byte_value'] = None
        return apkInfo
    except Exception as e:
        raise e

def extract_file_from_apk(file_path, file_of_interest, destination=None):
    try:
        extract_file = {'name': os.path.basename(file_of_interest),
                        'byte_value': None}
        with zipfile.ZipFile(file_path, 'r') as zipObj:
            extract_file['byte_value'] = zipObj.read(file_of_interest, pwd=None)
            if destination:
                pathlib.Path(destination).parent.mkdir(parents=True, exist_ok=True)
                zip_info = zipObj.getinfo(file_of_interest)
                zip_info.filename = extract_file['name']
                zipObj.extract(zip_info,
                               os.path.join(destination),
                               pwd=None)
            return extract_file
    except Exception as e:
        raise e
