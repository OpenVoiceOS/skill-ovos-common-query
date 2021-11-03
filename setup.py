#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'fallback-query.mycroftai=ovos_skill_common_query:QuestionsAnswersSkill'
# in this case the skill_id is defined to purposefully replace the mycroft version of the skill,
# or rather to be replaced by it in case it is present. all skill directories take precedence over plugin skills


setup(
    # this is the package name that goes on pip
    name='ovos-skill-common-query',
    version='0.0.1',
    description='OVOS common-query skill plugin',
    url='https://github.com/OpenVoiceOS/skill-ovos-common-query',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"ovos_skill_common_query": ""},
    package_data={'ovos_skill_common_query': ["locale/*"]},
    packages=['ovos_skill_common_query'],
    include_package_data=True,
    install_requires=["ovos-plugin-manager>=0.0.2", "astral==1.4", "arrow==0.12.0"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
