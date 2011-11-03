# revision 16184
# category Package
# catalog-ctan /biblio/bibtex/contrib/economic
# catalog-date 2009-11-25 18:21:28 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-economic
Version:	20091125
Release:	1
Summary:	BibTeX support for submitting to Economics journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/economic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/economic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/economic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle offers macros and BibTeX styles for the American
Economic Review (AER), the American Journal of Agricultural
Economics (AJAE), the Canadian Journal of Economics (CJE), the
European Review of Agricultural Economics (ERAE), the
International Economic Review (IER) and Economica. The macro
sets are based on (and require) the harvard package, and all
provide variations of author-date styles of presentation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/economic/aer.bst
%{_texmfdistdir}/bibtex/bst/economic/aertt.bst
%{_texmfdistdir}/bibtex/bst/economic/agecon.bst
%{_texmfdistdir}/bibtex/bst/economic/ajae.bst
%{_texmfdistdir}/bibtex/bst/economic/apecon.bst
%{_texmfdistdir}/bibtex/bst/economic/cje.bst
%{_texmfdistdir}/bibtex/bst/economic/ecca.bst
%{_texmfdistdir}/bibtex/bst/economic/econometrica-fr.bst
%{_texmfdistdir}/bibtex/bst/economic/econometrica.bst
%{_texmfdistdir}/bibtex/bst/economic/ecta.bst
%{_texmfdistdir}/bibtex/bst/economic/erae.bst
%{_texmfdistdir}/bibtex/bst/economic/ier.bst
%{_texmfdistdir}/bibtex/bst/economic/itaxpf.bst
%{_texmfdistdir}/bibtex/bst/economic/jae.bst
%{_texmfdistdir}/bibtex/bst/economic/jpe.bst
%{_texmfdistdir}/bibtex/bst/economic/jss2.bst
%{_texmfdistdir}/bibtex/bst/economic/oega.bst
%{_texmfdistdir}/bibtex/bst/economic/regstud.bst
%{_texmfdistdir}/bibtex/bst/economic/tandfx.bst
%{_texmfdistdir}/bibtex/bst/economic/worlddev.bst
%{_texmfdistdir}/tex/latex/economic/aer.sty
%{_texmfdistdir}/tex/latex/economic/aertt.sty
%{_texmfdistdir}/tex/latex/economic/agecon.cls
%{_texmfdistdir}/tex/latex/economic/ajae.cls
%{_texmfdistdir}/tex/latex/economic/apecon.cls
%{_texmfdistdir}/tex/latex/economic/cje.sty
%{_texmfdistdir}/tex/latex/economic/ecca.cls
%{_texmfdistdir}/tex/latex/economic/erae.cls
%{_texmfdistdir}/tex/latex/economic/itaxpf.cls
%{_texmfdistdir}/tex/latex/economic/jrurstud.cls
%{_texmfdistdir}/tex/latex/economic/njf.cls
%{_texmfdistdir}/tex/latex/economic/oegatb.cls
%{_texmfdistdir}/tex/latex/economic/pocoec.cls
%{_texmfdistdir}/tex/latex/economic/regstud.cls
%{_texmfdistdir}/tex/latex/economic/worlddev.cls
%doc %{_texmfdistdir}/doc/bibtex/economic/CHANGELOG
%doc %{_texmfdistdir}/doc/bibtex/economic/NEWS
%doc %{_texmfdistdir}/doc/bibtex/economic/README
%doc %{_texmfdistdir}/doc/bibtex/economic/aer-cje-ex.bib
%doc %{_texmfdistdir}/doc/bibtex/economic/aer-cje-ex.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/aer-natbib-ex.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/ajae-ex.bib
%doc %{_texmfdistdir}/doc/bibtex/economic/ajae-ex.pdf
%doc %{_texmfdistdir}/doc/bibtex/economic/ajae-ex.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/apecon-ex.bib
%doc %{_texmfdistdir}/doc/bibtex/economic/apecon-ex.pdf
%doc %{_texmfdistdir}/doc/bibtex/economic/apecon-ex.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/ecca-ex.bib
%doc %{_texmfdistdir}/doc/bibtex/economic/ecca-ex.pdf
%doc %{_texmfdistdir}/doc/bibtex/economic/ecca-ex.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/erae-ex.bib
%doc %{_texmfdistdir}/doc/bibtex/economic/erae-ex.pdf
%doc %{_texmfdistdir}/doc/bibtex/economic/erae-ex.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/ier-bib-test.pdf
%doc %{_texmfdistdir}/doc/bibtex/economic/ier-bib-test.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/ier-ex.bib
%doc %{_texmfdistdir}/doc/bibtex/economic/itaxpf-ex-title.pdf
%doc %{_texmfdistdir}/doc/bibtex/economic/itaxpf-ex-title.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/itaxpf-ex.bib
%doc %{_texmfdistdir}/doc/bibtex/economic/itaxpf-ex.pdf
%doc %{_texmfdistdir}/doc/bibtex/economic/itaxpf-ex.tex
%doc %{_texmfdistdir}/doc/bibtex/economic/oegatb-ex.bib
%doc %{_texmfdistdir}/doc/bibtex/economic/oegatb-ex.pdf
%doc %{_texmfdistdir}/doc/bibtex/economic/oegatb-ex.png
%doc %{_texmfdistdir}/doc/bibtex/economic/oegatb-ex.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
