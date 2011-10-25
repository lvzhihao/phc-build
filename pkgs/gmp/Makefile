include ../../support/include.mk
include ../version.mk

pkgname=${gmp_pkgname}
fileurl="http://mirror.bjtu.edu.cn/gnu/gmp/${pkgname}.tar.gz"

configargs=--prefix=${tmp_pkgs}/${pkgname}

all: ${pkgname}
    
${pkgname}: ../distfiles/${pkgname}.tar.gz
	tar xvf $<
	(cd ${pkgname}; ./configure ${configargs})
	$(MAKE) -C ${pkgname} all
	$(MAKE) -C ${pkgname} install

install:
    
../distfiles/${pkgname}.tar.gz:
	wget -O $@ ${fileurl}
	
clean:
	-rm -rf ${pkgname}
