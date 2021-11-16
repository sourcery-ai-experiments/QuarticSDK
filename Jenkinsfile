#!groovy

@Library('shared-library') _
import quarticpipeline.PipelineBuilder

containerNodes = [
  // Test: [
  //   dir: './jenkins_scripts/',
  //     steps: [
  //       test: [
  //         file_name: 'test.sh',
  //         docker_image: 'quarticai/python:3.9.5-slim-base',
  //         docker_image_args: '-u root'
  //           ]
  //       ]
  //   ],
  Publish: [
    dir: './jenkins_scripts/',
      steps: [
        publish: [
          file_name: 'publish.sh',
          docker_image: 'quarticai/python:3.9.5-slim-docker',
          docker_image_args: '-u root -v /var/run/docker.sock:/var/run/docker.sock'
            ]
        ]
    ]
]

pipelineBuilder = new PipelineBuilder(this, env, scm, containerNodes)
userEnv = ['RESERVE=azubuntu']

pipelineBuilder.executePipeline(userEnv)
