AC_INIT(phc, 1.0, lvzhihao@shopex.cn)

dnl todo: check perl

AC_CONFIG_FILES([support/include.mk  \
		 pkgs/Makefile	\
		 Makefile])

dnl work out who the cpu, vendor and OS are
AC_CANONICAL_SYSTEM
AC_DEFINE_UNQUOTED(CPU_VENDOR_OS, "$target", CPU_VENDOR_OS)

dnl Programs

AC_PROG_CC

AC_PROG_INSTALL

dnl C header files
AC_CHECK_LIB(expat, XML_ParserCreate, , AC_MSG_ERROR([* ** Unable to find expat libary ]))

AC_SUBST(LD_SHARED)
AC_OUTPUT()
