Name:           nvenc
Version:        8.0.14
Release:        1%{?dist}
Epoch:          1
Summary:        A comprehensive set of APIs for hardware accelerated video encode and decode

License:        https://developer.nvidia.com/nvidia-video-codec-sdk-license-agreement
URL:            https://developer.nvidia.com/nvidia-video-codec-sdk
Source0:        Video_Codec_SDK_%{version}.zip

BuildArch:      noarch

Provides:       nvidia-video-codec-sdk = %{?epoch}:%{version}-%{release}
Obsoletes:      nvidia-video-codec-sdk < %{?epoch}:%{version}-%{release}
Provides:       nvenc-devel = %{?epoch}:%{version}-%{release}
Obsoletes:      nvenc-devel < %{?epoch}:%{version}-%{release}

# Required for:
# - libnvcuvid.so (NVDECODE)
# - libnvidia-encode.so (NVENCODE)
Requires:       nvidia-driver-devel >= 2:378.13

%description
NVIDIA Products with the Kepler, Maxwell and Pascal generation GPUs contain a
dedicated accelerator for video encoding, called NVENC and a dedicated
accelerator for video decoding, called NVDEC, on the GPU die.

While using the dedicated hardware for encode or decode, the GPU’s CUDA cores
and system CPU are free to run other compute-intensive tasks.

NVENCODE API enables software developers to configure this dedicated hardware
video encoder. This dedicated accelerator encodes video at higher speeds and
power efficiency than CUDA-based or CPU-based encoders at equivalent quality.
NVENCODE API allows the programmer to control various settings of the encoder
to set the desired tradeoff between quality and performance.

NVDECODE API enables software developers to configure this dedicated hardware
video decoder. This dedicated accelerator supports hardware-accelerated decoding
of the following video codecs on Windows and Linux platforms: MPEG-2, VC-1,
H.264 (AVCHD), H.265 (HEVC), VP8, VP9.

%package samples
Summary:        nvEncoder Sample application source code
Requires:       %{name} = %{?epoch}:%{version}-%{release}

%description samples
This package contains nvEncoder Sample application source code demonstrating
various encoding capabilities.

%prep
%setup -q -n Video_Codec_SDK_%{version}

%install
mkdir -p %{_includedir}/%{name}
for h in nvEncodeAPI.h dynlink_cuviddec.h dynlink_nvcuvid.h; do
  install -m 644 -p Samples/common/inc/$h %{buildroot}%{_includedir}/%{name}/
  ln -sf %{_includedir}/%{name}/$h Samples/common/inc/$h
done

%files
%license LicenseAgreement.pdf
%doc doc/*.pdf Release_notes.txt ReadMe.txt
%{_includedir}/%{name}

%files samples
%doc Samples

%changelog
* Thu Jun 22 2017 Simone Caronni <negativo17@gmail.com> - 1:8.0.14-1
- Update to 8.0.14.
- Do not add license also to samples, as it requires the base package.
- Requires driver 378.13+.
- Add NVDECODE headers and require nvidia-driver-devel for unversioned shared
  libraries.

* Sun Jan 08 2017 Simone Caronni <negativo17@gmail.com> - 1:7.1.9-1
- Update to 7.1.9.

* Fri Aug 19 2016 Simone Caronni <negativo17@gmail.com> - 7.0.1-1
- Update to 7.0.1.
- Runtime requires drivers 367.35+ and adds support for Pascal GPUs.

* Wed Jan 06 2016 Simone Caronni <negativo17@gmail.com> - 6.0.1-1
- Update to 6.0.1.

* Fri Apr 10 2015 Simone Caronni <negativo17@gmail.com> - 5.0.1-1
- First build.
