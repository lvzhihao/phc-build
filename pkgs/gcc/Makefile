include ../../support/include.mk
include ../version.mk

pkgname=${gcc_pkgname}
fileurl="http://mirrors.ustc.edu.cn/gnu/gcc/${pkgname}/${pkgname}.tar.bz2"

ldlibpath=LD_LIBRARY_PATH=${tmp_pkgs}/${gmp_pkgname}/lib:${tmp_pkgs}/${mpfr_pkgname}/lib:${LD_LIBRARY_PATH}

configargs=--prefix=${tmp_pkgs}/${pkgname} \
            --enable-languages=c,c++ \
	    --with-mpfr=${tmp_pkgs}/${mpfr_pkgname} \
	    --with-gmp=${tmp_pkgs}/${gmp_pkgname} \
	    --with-mpfr-lib=${tmp_pkgs}/${mpfr_pkgname}/lib/ \
	    --with-gmp-lib=${tmp_pkgs}/${gmp_pkgname}/lib/ \
	    --with-mpfr-include=${tmp_pkgs}/${mpfr_pkgname}/include/ \
	    --with-gmp-include=${tmp_pkgs}/${gmp_pkgname}/include/



all: ${pkgname}
    
${pkgname}: ../distfiles/${pkgname}.tar.bz2
	tar xvjf $<
	(cd ${pkgname}; ./configure ${configargs})
	$(MAKE) ${ldlibpath} -C ${pkgname} all
	$(MAKE) ${ldlibpath} -C ${pkgname} install

install:
    
../distfiles/${pkgname}.tar.bz2:
	wget -O $@ ${fileurl}
	
clean:
	-rm -rf ${pkgname}
