include ../../support/include.mk
include ../version.mk

pkgname=${gc_pkgname}
fileurl="http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/${pkgname}.tar.gz"

configargs=--prefix=${tmp_pkgs}/${pkgname}  \
	    --enable-cplusplus

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
