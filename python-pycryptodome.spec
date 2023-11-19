#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pycryptodome
Summary:	Package of low-level cryptographic primitives
Summary(pl.UTF-8):	Pakiet niskopoziomowych funkcji kryptograficznych
Name:		python-%{module}
Version:	3.19.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pycryptodome/%{module}-%{version}.tar.gz
# Source0-md5:	b6f99715010bbb3f5e0400adc0063dfb
URL:		https://www.pycryptodome.org/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3 >= 4.5
# >= 7.1.0 when available
%endif
Requires:	python-modules >= 1:2.7
Conflicts:	python-Crypto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyCryptodomex is a fork of PyCrypto. It brings the following
enhancements with respect to the last official version of PyCrypto
(2.6.1):
- Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
- Accelerated AES on Intel platforms via AES-NI
- First class support for PyPy
- Elliptic curves cryptography (NIST P-256, P-384 and P-521 curves
  only)
- Better and more compact API (nonce and iv attributes for ciphers,
  automatic generation of random nonces and IVs, simplified CTR cipher
  mode, and more)
- SHA-3 (including SHAKE XOFs), truncated SHA-512 and BLAKE2 hash
  algorithms
- Salsa20 and ChaCha20/XChaCha20 stream ciphers
- Poly1305 MAC
- ChaCha20-Poly1305 and XChaCha20-Poly1305 authenticated ciphers
- scrypt, bcrypt and HKDF derivation functions
- Deterministic (EC)DSA
- Password-protected PKCS#8 key containers
- Shamir's Secret Sharing scheme
- Random numbers get sourced directly from the OS (and not from a
  CSPRNG in userspace)
- Simplified install process, including better support for Windows
- Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
- Major clean ups and simplification of the code base

Pycryptodome module is available under the Crypto package.

%description -l pl.UTF-8
PyCryptodomex to odgałęzienie PyCrypto. Dostarcza następujące
rozszerzenia w stosunku do ostatniej oficjalnej wersji PyCrypto
(2.6.1):
- uwierzytelniane tryby szyfrowania (GCM, CCM, EAX, SIV, OCB)
- akcelerowane szyfrowanie AES na platformach Intela poprzez AES-NI
- dobra obsługa PyPy
- kryptografia krzywych eliptycznych (tylko NIST P-256, P-384, P-521)
- lepsze i bardziej kompaktowe API (atrybuty nonce i iv dla szyfrów,
  automatyczne generowanie losowych nonce i IV, uproszczony tryb
  szyfrowania CTR itp.)
- SHA-3 (w tym SHAKE XOF), skrócone algorytmy SHA-512 i BLAKE2
- szyfry strumieniowe Salsa20 i ChaCha20/XChaCha20
- MAC Poly1305
- szyfry uwierzytelniane ChaCha20-Poly1305 i XChaCha20-Poly1305
- funkcje pochodne scrypt, bcrypt i HKDF
- deterministyczne (EC)DSA
- kontenery kluczy PKCS#8 chronione hasłem
- schemat Shamir's Secret Sharing
- liczby losowe pochodzące bezpośrednio z systemu operacyjnego
  (zamiast CSPRNG w przestrzeni użytkownika)
- uproszczony proces instalacji, w tym lepsza obsługa Windows
- czystsze generowanie kluczy RSA i DSA (oparte głównie na FIPS 186-4)
- spore oczyszczenie i uproszczenie kodu

Moduł pycryptodome jest dostępny pod nazwą pakietu Crypto.

%package -n python3-%{module}
Summary:	Package of low-level cryptographic primitives
Summary(pl.UTF-8):	Pakiet niskopoziomowych funkcji kryptograficznych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5
Conflicts:	python3-Crypto

%description -n python3-%{module}
PyCryptodomex is a fork of PyCrypto. It brings the following
enhancements with respect to the last official version of PyCrypto
(2.6.1):
- Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
- Accelerated AES on Intel platforms via AES-NI
- First class support for PyPy
- Elliptic curves cryptography (NIST P-256, P-384 and P-521 curves
  only)
- Better and more compact API (nonce and iv attributes for ciphers,
  automatic generation of random nonces and IVs, simplified CTR cipher
  mode, and more)
- SHA-3 (including SHAKE XOFs), truncated SHA-512 and BLAKE2 hash
  algorithms
- Salsa20 and ChaCha20/XChaCha20 stream ciphers
- Poly1305 MAC
- ChaCha20-Poly1305 and XChaCha20-Poly1305 authenticated ciphers
- scrypt, bcrypt and HKDF derivation functions
- Deterministic (EC)DSA
- Password-protected PKCS#8 key containers
- Shamir's Secret Sharing scheme
- Random numbers get sourced directly from the OS (and not from a
  CSPRNG in userspace)
- Simplified install process, including better support for Windows
- Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
- Major clean ups and simplification of the code base

Pycryptodome module is available under the Crypto package.

%description -n python3-%{module} -l pl.UTF-8
PyCryptodomex to odgałęzienie PyCrypto. Dostarcza następujące
rozszerzenia w stosunku do ostatniej oficjalnej wersji PyCrypto
(2.6.1):
- uwierzytelniane tryby szyfrowania (GCM, CCM, EAX, SIV, OCB)
- akcelerowane szyfrowanie AES na platformach Intela poprzez AES-NI
- dobra obsługa PyPy
- kryptografia krzywych eliptycznych (tylko NIST P-256, P-384, P-521)
- lepsze i bardziej kompaktowe API (atrybuty nonce i iv dla szyfrów,
  automatyczne generowanie losowych nonce i IV, uproszczony tryb
  szyfrowania CTR itp.)
- SHA-3 (w tym SHAKE XOF), skrócone algorytmy SHA-512 i BLAKE2
- szyfry strumieniowe Salsa20 i ChaCha20/XChaCha20
- MAC Poly1305
- szyfry uwierzytelniane ChaCha20-Poly1305 i XChaCha20-Poly1305
- funkcje pochodne scrypt, bcrypt i HKDF
- deterministyczne (EC)DSA
- kontenery kluczy PKCS#8 chronione hasłem
- schemat Shamir's Secret Sharing
- liczby losowe pochodzące bezpośrednio z systemu operacyjnego
  (zamiast CSPRNG w przestrzeni użytkownika)
- uproszczony proces instalacji, w tym lepsza obsługa Windows
- czystsze generowanie kluczy RSA i DSA (oparte głównie na FIPS 186-4)
- spore oczyszczenie i uproszczenie kodu

Moduł pycryptodome jest dostępny pod nazwą pakietu Crypto.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(echo $(pwd)/build-3/lib.linux-*) \
%{__make} -C Doc html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc {AUTHORS,Changelog,FuturePlans,README}.rst
%dir %{py_sitedir}/Crypto
%{py_sitedir}/Crypto/*.py[coi]
%{py_sitedir}/Crypto/py.typed
%dir %{py_sitedir}/Crypto/Cipher
%{py_sitedir}/Crypto/Cipher/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Crypto/Cipher/*.so
%dir %{py_sitedir}/Crypto/Hash
%{py_sitedir}/Crypto/Hash/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Crypto/Hash/*.so
%{py_sitedir}/Crypto/IO
%dir %{py_sitedir}/Crypto/Math
%{py_sitedir}/Crypto/Math/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Crypto/Math/*.so
%dir %{py_sitedir}/Crypto/Protocol
%{py_sitedir}/Crypto/Protocol/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Crypto/Protocol/*.so
%dir %{py_sitedir}/Crypto/PublicKey
%{py_sitedir}/Crypto/PublicKey/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Crypto/PublicKey/*.so
%{py_sitedir}/Crypto/Random
%{py_sitedir}/Crypto/SelfTest
%{py_sitedir}/Crypto/Signature
%dir %{py_sitedir}/Crypto/Util
%{py_sitedir}/Crypto/Util/*.py[coi]
%attr(755,root,root) %{py_sitedir}/Crypto/Util/*.so
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc {AUTHORS,Changelog,FuturePlans,README}.rst
%dir %{py3_sitedir}/Crypto
%{py3_sitedir}/Crypto/*.py
%{py3_sitedir}/Crypto/*.pyi
%{py3_sitedir}/Crypto/py.typed
%{py3_sitedir}/Crypto/__pycache__
%dir %{py3_sitedir}/Crypto/Cipher
%{py3_sitedir}/Crypto/Cipher/*.py
%{py3_sitedir}/Crypto/Cipher/*.pyi
%{py3_sitedir}/Crypto/Cipher/__pycache__
%attr(755,root,root) %{py3_sitedir}/Crypto/Cipher/*.so
%dir %{py3_sitedir}/Crypto/Hash
%{py3_sitedir}/Crypto/Hash/*.py
%{py3_sitedir}/Crypto/Hash/*.pyi
%{py3_sitedir}/Crypto/Hash/__pycache__
%attr(755,root,root) %{py3_sitedir}/Crypto/Hash/*.so
%{py3_sitedir}/Crypto/IO
%dir %{py3_sitedir}/Crypto/Math
%{py3_sitedir}/Crypto/Math/*.py
%{py3_sitedir}/Crypto/Math/*.pyi
%{py3_sitedir}/Crypto/Math/__pycache__
%attr(755,root,root) %{py3_sitedir}/Crypto/Math/*.so
%dir %{py3_sitedir}/Crypto/Protocol
%{py3_sitedir}/Crypto/Protocol/*.py
%{py3_sitedir}/Crypto/Protocol/*.pyi
%{py3_sitedir}/Crypto/Protocol/__pycache__
%attr(755,root,root) %{py3_sitedir}/Crypto/Protocol/*.so
%dir %{py3_sitedir}/Crypto/PublicKey
%{py3_sitedir}/Crypto/PublicKey/*.py
%{py3_sitedir}/Crypto/PublicKey/*.pyi
%{py3_sitedir}/Crypto/PublicKey/__pycache__
%attr(755,root,root) %{py3_sitedir}/Crypto/PublicKey/*.so
%{py3_sitedir}/Crypto/Random
%{py3_sitedir}/Crypto/SelfTest
%{py3_sitedir}/Crypto/Signature
%dir %{py3_sitedir}/Crypto/Util
%{py3_sitedir}/Crypto/Util/*.py
%{py3_sitedir}/Crypto/Util/*.pyi
%{py3_sitedir}/Crypto/Util/__pycache__
%attr(755,root,root) %{py3_sitedir}/Crypto/Util/*.so
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc Doc/_build/html/{_images,_static,src,*.html,*.js}
%endif
