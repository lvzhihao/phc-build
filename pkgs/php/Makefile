include ../../support/include.mk
include ../version.mk

pkgname=${php_pkgname}
fileurl="http://museum.php.net/php5/${pkgname}.tar.bz2"

configargs=--prefix=${tmp_pkgs}/${pkgname} \
			--enable-embed 

all: ${pkgname}
    
${pkgname}: ../distfiles/${pkgname}.tar.bz2
	tar xvjf $<
	(cd ${pkgname}; ./configure ${configargs})
	$(MAKE) -C ${pkgname} all
	$(MAKE) -C ${pkgname} install

install:
    
../distfiles/${pkgname}.tar.bz2:
	wget -O $@ ${fileurl}
	
clean:
	-rm -rf ${pkgname}
