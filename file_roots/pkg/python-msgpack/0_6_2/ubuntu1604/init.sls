{% import "setup/ubuntu/map.jinja" as buildcfg %}
{% set force = salt['pillar.get']('build_force.all', False) or salt['pillar.get']('build_force.' ~ slspath, False) %}

{% set pypi_name = 'msgpack' %}
{% set name = 'python-' ~ pypi_name %}
{% set name3 = 'python3-' ~ pypi_name %}
{% set rname = pypi_name ~ '-python'%}
{% set version = '0.6.2' %}
{% set release_nameadd = '' %}
{% set release_ver = '1' %}

{{name}}-{{version.replace('.', '_')}}:
  pkgbuild.built:
    - runas: {{buildcfg.build_runas}}
    - results: 
      - {{name3}}_{{version}}-{{release_ver}}{{release_nameadd}}_{{buildcfg.build_arch}}.deb
      - {{rname}}_{{version}}.orig.tar.gz
      - {{rname}}_{{version}}-{{release_ver}}{{release_nameadd}}.debian.tar.xz
      - {{rname}}_{{version}}-{{release_ver}}{{release_nameadd}}.dsc
    - force: {{force}}
    - dest_dir: {{buildcfg.build_dest_dir}}
    - spec: salt://{{slspath}}/spec/{{rname}}_{{version}}-{{release_ver}}{{release_nameadd}}.dsc
    - tgt: {{buildcfg.build_tgt}}
    - env:
        DEB_BUILD_OPTIONS : 'nocheck'
    - template: jinja
    - sources:
      - salt://{{slspath}}/sources/{{rname}}_{{version}}.orig.tar.gz
      - salt://{{slspath}}/sources/{{rname}}_{{version}}-{{release_ver}}{{release_nameadd}}.debian.tar.xz
