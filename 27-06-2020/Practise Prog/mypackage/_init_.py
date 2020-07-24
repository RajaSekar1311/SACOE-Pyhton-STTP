Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help('modules')

Please wait a moment while I gather a list of all available modules...

__future__          _tracemalloc        hashlib             run
__main__            _warnings           heapq               runpy
_ast                _weakref            hello               runscript
_asyncio            _weakrefset         help                sched
_asyncio_d          _winapi             help_about          scrolledlist
_bisect             abc                 history             search
_blake2             aifc                hmac                searchbase
_bootlocale         antigravity         html                searchengine
_bz2                argparse            http                secrets
_bz2_d              array               hyperparser         select
_codecs             ast                 idle                select_d
_codecs_cn          asynchat            idle_test           selectors
_codecs_hk          asyncio             idlelib             shelve
_codecs_iso2022     asyncore            imaplib             shlex
_codecs_jp          atexit              imghdr              shutil
_codecs_kr          audioop             imp                 signal
_codecs_tw          autocomplete        importlib           site
_collections        autocomplete_w      inspect             smtpd
_collections_abc    autoexpand          io                  smtplib
_compat_pickle      base64              iomenu              sndhdr
_compression        bdb                 ipaddress           socket
_csv                binascii            itertools           socketserver
_ctypes             binhex              json                sqlite3
_ctypes_d           bisect              keyword             sre_compile
_ctypes_test        browser             lib2to3             sre_constants
_ctypes_test_d      builtins            linecache           sre_parse
_datetime           bz2                 locale              ssl
_decimal            cProfile            logging             stackviewer
_decimal_d          calendar            lzma                stat
_dummy_thread       calltip_w           macosx              statistics
_elementtree        calltips            macpath             statusbar
_elementtree_d      cgi                 macurl2path         string
_findvs             cgitb               mailbox             stringprep
_functools          chunk               mailcap             struct
_hashlib            cmath               mainmenu            subprocess
_hashlib_d          cmd                 marshal             sunau
_heapq              code                math                symbol
_imp                codecontext         mimetypes           symtable
_io                 codecs              mmap                sys
_json               codeop              modulefinder        sysconfig
_locale             collections         msilib              tabnanny
_lsprof             colorizer           msvcrt              tarfile
_lzma               colorsys            multicall           telnetlib
_lzma_d             compileall          multiprocessing     tempfile
_markupbase         concurrent          netrc               test
_md5                config              nntplib             textview
_msi                config_key          nt                  textwrap
_msi_d              configdialog        ntpath              this
_multibytecodec     configparser        nturl2path          threading
_multiprocessing    contextlib          numbers             time
_multiprocessing_d  copy                opcode              timeit
_opcode             copyreg             operator            tkinter
_operator           crypt               optparse            token
_osx_support        csv                 os                  tokenize
_overlapped         ctypes              outwin              tooltip
_overlapped_d       curses              paragraph           trace
_pickle             datetime            parenmatch          traceback
_pyclbr             dbm                 parser              tracemalloc
_pydecimal          debugger            pathbrowser         tree
_pyio               debugger_r          pathlib             tty
_random             debugobj            pdb                 turtle
_sha1               debugobj_r          percolator          turtledemo
_sha256             decimal             pickle              types
_sha3               delegator           pickletools         typing
_sha512             difflib             pipes               undo
_signal             dis                 pkgutil             unicodedata
_sitebuiltins       distutils           platform            unicodedata_d
_socket             doctest             plistlib            unittest
_socket_d           dummy_threading     poplib              urllib
_sqlite3            dynoption           posixpath           uu
_sqlite3_d          editor              pprint              uuid
_sre                email               profile             venv
_ssl                encodings           pstats              warnings
_ssl_d              ensurepip           pty                 wave
_stat               enum                py_compile          weakref
_string             errno               pyclbr              webbrowser
_strptime           faulthandler        pydoc               windows
_struct             filecmp             pydoc_data          winreg
_symtable           fileinput           pyexpat             winsound
_testbuffer         filelist            pyexpat_d           winsound_d
_testbuffer_d       fnmatch             pyparse             wsgiref
_testcapi           formatter           pyshell             xdrlib
_testcapi_d         fractions           query               xml
_testconsole        ftplib              queue               xmlrpc
_testconsole_d      functools           quopri              xxsubtype
_testimportmultiple gc                  random              zipapp
_testimportmultiple_d genericpath         re                  zipfile
_testmultiphase     getopt              redirector          zipimport
_testmultiphase_d   getpass             replace             zlib
_thread             gettext             reprlib             zoomheight
_threading_local    glob                rlcompleter         zzdummy
_tkinter            grep                rpc                 
_tkinter_d          gzip                rstrip              

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

>>> dir('math')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help('math')
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)
        
        Return the arc cosine (measured in radians) of x.
    
    acosh(...)
        acosh(x)
        
        Return the inverse hyperbolic cosine of x.
    
    asin(...)
        asin(x)
        
        Return the arc sine (measured in radians) of x.
    
    asinh(...)
        asinh(x)
        
        Return the inverse hyperbolic sine of x.
    
    atan(...)
        atan(x)
        
        Return the arc tangent (measured in radians) of x.
    
    atan2(...)
        atan2(y, x)
        
        Return the arc tangent (measured in radians) of y/x.
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(...)
        atanh(x)
        
        Return the inverse hyperbolic tangent of x.
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as an Integral.
        This is the smallest integer >= x.
    
    copysign(...)
        copysign(x, y)
        
        Return a float with the magnitude (absolute value) of x but the sign 
        of y. On platforms that support signed zeros, copysign(1.0, -0.0) 
        returns -1.0.
    
    cos(...)
        cos(x)
        
        Return the cosine of x (measured in radians).
    
    cosh(...)
        cosh(x)
        
        Return the hyperbolic cosine of x.
    
    degrees(...)
        degrees(x)
        
        Convert angle x from radians to degrees.
    
    erf(...)
        erf(x)
        
        Error function at x.
    
    erfc(...)
        erfc(x)
        
        Complementary error function at x.
    
    exp(...)
        exp(x)
        
        Return e raised to the power of x.
    
    expm1(...)
        expm1(x)
        
        Return exp(x)-1.
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(...)
        fabs(x)
        
        Return the absolute value of the float x.
    
    factorial(...)
        factorial(x) -> Integral
        
        Find x!. Raise a ValueError if x is negative or non-integral.
    
    floor(...)
        floor(x)
        
        Return the floor of x as an Integral.
        This is the largest integer <= x.
    
    fmod(...)
        fmod(x, y)
        
        Return fmod(x, y), according to platform C.  x % y may differ.
    
    frexp(...)
        frexp(x)
        
        Return the mantissa and exponent of x, as pair (m, e).
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(...)
        fsum(iterable)
        
        Return an accurate floating point sum of values in the iterable.
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(...)
        gamma(x)
        
        Gamma function at x.
    
    gcd(...)
        gcd(x, y) -> int
        greatest common divisor of x and y
    
    hypot(...)
        hypot(x, y)
        
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(...)
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool
        
        Determine whether two floating point numbers are close in value.
        
           rel_tol
               maximum difference for being considered "close", relative to the
               magnitude of the input values
            abs_tol
               maximum difference for being considered "close", regardless of the
               magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(...)
        isfinite(x) -> bool
        
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(...)
        isinf(x) -> bool
        
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(...)
        isnan(x) -> bool
        
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(...)
        ldexp(x, i)
        
        Return x * (2**i).
    
    lgamma(...)
        lgamma(x)
        
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x[, base])
        
        Return the logarithm of x to the given base.
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(...)
        log10(x)
        
        Return the base 10 logarithm of x.
    
    log1p(...)
        log1p(x)
        
        Return the natural logarithm of 1+x (base e).
        The result is computed in a way which is accurate for x near zero.
    
    log2(...)
        log2(x)
        
        Return the base 2 logarithm of x.
    
    modf(...)
        modf(x)
        
        Return the fractional and integer parts of x.  Both results carry the sign
        of x and are floats.
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    
    radians(...)
        radians(x)
        
        Convert angle x from degrees to radians.
    
    sin(...)
        sin(x)
        
        Return the sine of x (measured in radians).
    
    sinh(...)
        sinh(x)
        
        Return the hyperbolic sine of x.
    
    sqrt(...)
        sqrt(x)
        
        Return the square root of x.
    
    tan(...)
        tan(x)
        
        Return the tangent of x (measured in radians).
    
    tanh(...)
        tanh(x)
        
        Return the hyperbolic tangent of x.
    
    trunc(...)
        trunc(x:Real) -> Integral
        
        Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> import math
>>> math.sqrt(4)
2.0
>>> math.pow(2,3)
8.0
>>> 
== RESTART: C:/Users/SYS/Desktop/SACOE Python FDP/27-06-2020/calculator.py ==
>>> import calc
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    import calc
ModuleNotFoundError: No module named 'calc'
>>> calc.add(2,5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    calc.add(2,5)
NameError: name 'calc' is not defined
>>> import calculator
>>> calculator.add(2,3)
5
>>> calculator.mul(3,78)
234
>>> del(calculator)
>>> calculator.add(2,3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    calculator.add(2,3)
NameError: name 'calculator' is not defined
>>> 
