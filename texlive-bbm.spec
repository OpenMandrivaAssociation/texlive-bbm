%global tl_name bbm
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Blackboard-style cm fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cm/bbm
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Blackboard variants of Computer Modern fonts. The fonts are distributed
as Metafont source (only); LaTeX support is available with the bbm-
macros package. The Sauter font package has Metafont parameter source
files for building the fonts at more sizes than you could reasonably
imagine. A sample of these fonts appears in the blackboard bold sampler.

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
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/doc/fonts/bbm
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/source/public/bbm
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bbm
%doc %{_datadir}/texmf-dist/doc/fonts/bbm/README
%doc %{_datadir}/texmf-dist/doc/fonts/bbm/gfbatch.batch
%doc %{_datadir}/texmf-dist/doc/fonts/bbm/mfbatch.batch
%doc %{_datadir}/texmf-dist/doc/fonts/bbm/test.tex
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbm10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbm12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbm17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbm5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbm6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbm7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbm8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbm9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmbx10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmbx12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmbx5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmbx6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmbx7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmbx8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmbx9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmbxsl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmdunh10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmfib8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmfxib8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbminch.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmsl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmsl12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmsl8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmsl9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmsltt10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmss10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmss12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmss17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmss8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmss9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssbx10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssdc10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssi10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssi12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssi17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssi8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssi9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssq8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmssqi8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmtt10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmtt12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmtt8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmtt9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/bbmvtt10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/blbbase.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/blbord.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/blbordl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/blbordsp.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbm/blbordu.mf
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbm10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbm12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbm17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbm5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbm6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbm7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbm8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbm9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmbx10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmbx12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmbx5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmbx6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmbx7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmbx8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmbx9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmbxsl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmdunh10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmfib8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmfxib8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmsl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmsl12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmsl8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmsl9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmss10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmss12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmss17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmss8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmss9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssbx10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssdc10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssi12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssi17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssi8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssi9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssq8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmssqi8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmtt10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmtt12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmtt8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbm/bbmtt9.tfm
