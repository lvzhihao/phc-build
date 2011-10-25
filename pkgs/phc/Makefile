include ../../support/include.mk
include ../version.mk

pkgname=${phc_pkgname}
fileurl="http://phc.googlecode.com/svn/trunk/"

ldlibpath=LD_LIBRARY_PATH=${tmp_pkgs}/${gmp_pkgname}/lib:${tmp_pkgs}/${mpfr_pkgname}/lib:${LD_LIBRARY_PATH}

configargs=--prefix=${prefix} \
		 --with-php=${tmp_pkgs}/${php_pkgname} \
		 --with-boost=${tmp_pkgs}/${boost_pkgname} \
		 --with-boost-libdir=${tmp_pkgs}/${boost_pkgname}/lib/ \
		 CC=${tmp_pkgs}/${gcc_pkgname}/bin/gcc \
		 CXX=${tmp_pkgs}/${gcc_pkgname}/bin/g++ 


all: ${pkgname}
    
${pkgname}: ../distfiles/${pkgname}
	cp -r $< ./
	(cd ${pkgname}; ./configure ${configargs} ${ldlibpath} CPPFLAGS="-I${tmp_pkgs}/${gc_pkgname}/include" LDFLAGS="-L${tmp_pkgs}/${gc_pkgname}/lib")
	(cd ${pkgname}; touch src/generated/{AST,HIR,MIR,MICG}*; touch src/generated/cmdline.{c,h}; touch src/generated/lex.yy.cc)
	patch -p0 < optimize.cpp.patch 
	$(MAKE) ${ldlibpath} -C ${pkgname} all

static_test:
	(cd ${pkgname}; rm -rf ./src/phc; /bin/sh ./libtool --tag=CXX --mode=link ${tmp_pkgs}/${gcc_pkgname}/bin/g++ \
	-all-static -Wextra -Wno-unused-parameter -Wno-write-strings -Wno-deprecated -g -O2 \
	-export-dynamic -L${tmp_pkgs}/${gc_pkgname}/lib -o src/phc phc.o -lgc -lgccpp libltdl/libltdlc.la \
	-lboost_regex libphc.la  -lgccpp -lgc -lphp5 -L${tmp_pkgs}/${php_pkgname}/lib -R${tmp_pkgs}/${php_pkgname}/lib \
	-lboost_regex -L${tmp_pkgs}/${boost_pkgname}/lib -R${tmp_pkgs}/${boost_pkgname}/lib -lresolv -ldl && echo "create static OK")

install:
	$(MAKE) DESTDIR=${DESTDIR} ${ldlibpath} -C ${pkgname} install

lddfix:
	LD_LIBRARY_PATH=${tmp_pkgs}/${boost_pkgname}/lib:$LD_LIBRARY_PATH ldd ${prefix}/bin/phc | \
	awk '{if ($$3 ~ /^${tmp_ext_pkgs}[^ (]/) print $$3}' | sort | uniq  | \
	xargs -I ’{}’ cp ’{}’ ${prefix}/lib/ 	

rpmbuildfix:
	LD_LIBRARY_PATH=${tmp_pkgs}/${boost_pkgname}/lib:$LD_LIBRARY_PATH ldd ${DESTDIR}/${prefix}/bin/phc | \
	awk '{if ($$3 ~ /^${tmp_ext_pkgs}[^ (]/) print $$3}' | sort | uniq  | \
	xargs -I ’{}’ cp ’{}’ ${DESTDIR}/${prefix}/lib/ 	
    
../distfiles/${pkgname}:
	svn checkout -r ${phc_version} ${fileurl} $@ 
	
clean:
	-rm -rf ${pkgname}
