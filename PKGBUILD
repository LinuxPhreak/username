# Maintainer: Ben P. Dorsi-Todaro <ben@bigbenshosting.com>
#I get the following errors when building
#==> ERROR: pkgver is not allowed to be empty.
#==> ERROR: pkgver() generated an invalid version:
_pkgbasename=username
pkgname=$_pkgbasename
pkgrel=1
pkgver=v1.0.r5.gf30f628
pkgdesc="Get Username information"
arch=('any')
url="https://linuxphreak.github.io/username"
license=('GPL')
depends=('python' 'python-requests' 'python-beautifulsoup4')
source=(git+https://github.com/LinuxPhreak/username)
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$_pkgbasename"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "$srcdir/$_pkgbasename"
    
    python setup.py bdist
}


package() {
    _pkg=$(ls "$srcdir/$_pkgbasename/dist/")
    tar -xC "$pkgdir/" -f "$srcdir/$_pkgbasename/dist/$_pkg"

    mkdir "$pkgdir/usr/bin"

    _python=$(ls "$pkgdir/usr/bin/")
    cp "$srcdir/$_pkgbasename/$_pkgbasename.py" "$pkgdir/usr/bin/$_pkgbasename"
    chmod +x "$pkgdir/usr/bin/$_pkgbasename"
    #ln -s "/usr/lib/$_python/site-packages/$_pkgbasename/$_pkgbasename.py" "$pkgdir/usr/bin/username.py"

}