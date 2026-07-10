%global tl_name akktex
%global tl_revision 26055

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.2
Release:	%{tl_revision}.1
Summary:	A collection of packages and classes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/akktex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/akktex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/akktex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides: new document classes for technical documents,
thesis works, manuscripts and lecture notes; many mathematical packages
providing a large number of macros for mathematical texts; layout
providing a non-empty parskip with extended length corrections and new
section definition commands; easy label creation for counters; and
german language tools and predefined abbreviations.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/akktex
%dir %{_datadir}/texmf-dist/tex/latex/akktex
%doc %{_datadir}/texmf-dist/doc/latex/akktex/README
%doc %{_datadir}/texmf-dist/doc/latex/akktex/README.TEXLIVE
%{_datadir}/texmf-dist/tex/latex/akktex/akkconditional.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkcounterlabelpattern.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkcs.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkdoc.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkgerman.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkgermanabbreviations.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akklecture.cls
%{_datadir}/texmf-dist/tex/latex/akktex/akklongpage.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmath.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathbasic.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathdisc.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathfun.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathnum.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathpaper.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathproof.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathrel.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathset.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkmathtext.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akknum.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkparskip.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkscript.cls
%{_datadir}/texmf-dist/tex/latex/akktex/akksection.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkstring.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akktecdoc.cls
%{_datadir}/texmf-dist/tex/latex/akktex/akktex.sty
%{_datadir}/texmf-dist/tex/latex/akktex/akkwidepage.sty
