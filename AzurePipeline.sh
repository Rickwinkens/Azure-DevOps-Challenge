#!/bin/bash
stages:
  - build
  - deploy_to_tomcat

build:
  stage: build
    script:
      - mvn clean build

deploy_to_tomcat:
  stage: deploy_to_tomcat
     script:
      - mvn deploy
      - sudo rm -rf /opt/tomcat/apache-tomcat-9.0.76/webapps/petclinic*
      - sudo cp -r target/petclinic.war /opt/tomcat/apache-tomcat-9.0.76/webapps

only:
  - master
