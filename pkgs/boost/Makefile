include ../../support/include.mk
include ../version.mk

pkgname=${boost_pkgname}
fileurl="http://downloads.sourceforge.net/project/boost/boost/${boost_version}/${pkgname}.tar.gz"

ldlibpath=LD_LIBRARY_PATH=${tmp_pkgs}/${gmp_pkgname}/lib:${tmp_pkgs}/${mpfr_pkgname}/lib:${LD_LIBRARY_PATH}

all: ${pkgname}/boost
    
${pkgname}: ../distfiles/${pkgname}.tar.gz
	tar xvf $<

${pkgname}/boost: ${pkgname}
	(cd ${pkgname}; ./bootstrap.sh; \
	${ldlibpath} PATH="${tmp_pkgs}/${gcc_pkgname}/bin:${PATH}" ./b2 install --prefix=${tmp_pkgs}/${pkgname} --toolset=${gcc_pkgname})

install:
    
../distfiles/${pkgname}.tar.gz:
	wget -O $@ ${fileurl}
	
clean:
	-rm -rf ${pkgname}
