# Maintainer: Ben P. Dorsi-Todaro <ben@bigbenshosting.com>
pkgname=username
_pkgname=$pkgname
pkgver=1.0.0
pkgrel=1
provides=("$_pkgname")
conflicts=("$_pkgname")
pkgdesc="Get Username information"
url="https://github.com/LinuxPhreak/$_pkgname"
arch=("any")
license=("GPL3")
depends=('python>=3' 'python-requests' 'python-beautifulsoup4')
source=("git+https://github.com/LinuxPhreak/$_pkgname.git")
md5sums=("SKIP")

pkgver()
{
    echo $pkgver 
}

package()
{
  cd "$_pkgname"
  python setup.py install --root="$pkgdir"
}