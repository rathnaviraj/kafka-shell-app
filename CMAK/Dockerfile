FROM openjdk:11

LABEL AUTHOR="Supun Viraj"
LABEL AUTHOR_EMAIL="rathnavira@gmail.com"
LABEL GITHUB="https://github.com/rathnaviraj"
LABEL GITHUB_CMAK="https://github.com/yahoo/CMAK"

ENV CMAK_VERSION=3.0.0.6

RUN cd /tmp && wget https://github.com/yahoo/CMAK/archive/${CMAK_VERSION}.tar.gz && tar -xzvf ${CMAK_VERSION}.tar.gz

RUN cd /tmp/CMAK-${CMAK_VERSION} && ./sbt clean dist

RUN unzip -d / /tmp/CMAK-${CMAK_VERSION}/target/universal/cmak-${CMAK_VERSION}.zip

RUN rm -fr /tmp/CMAK-${CMAK_VERSION} /tmp/${CMAK_VERSION}.tar.gz

WORKDIR /cmak-${CMAK_VERSION}

EXPOSE 9000

ENTRYPOINT ["./bin/cmak","-Dconfig.file=conf/application.conf"]