# application-firewall

## About
The Application Firewall package contains the interactive firewall used in the Dapper Linux distribution. 

## Building
To build this package, first install an RPM development chain:

```bash
$ sudo dnf install fedora-packager fedora-review

```

Next, setup rpmbuild directories with

```bash
$ rpmdev-setuptree
```
And place the file application-firewall.spec in the SPECS directory, and add all the files into a folder called fw-daemon and wrap it in a folder called application-firewall-1 and compress it:
```bash
$ mv application-firewall.spec ~/rpmbuild/SPECS/
$ mv sgfw.conf ~/rpmbuild/SOURCES
$ mkdir -p ~/rpmbuild/SOURCES/application-firewall-1/fw-daemon
$ mv * ~/rpmbuild/SOURCES/application-firewall-1/fw-daemon
$ cd ~/rpmbuild/SOURCES
$ tar -czvf application-firewall-1.tar.gz application-firewall-1
```

and finally, you can build RPMs and SRPMs with:
```bash
$ cd ~/rpmbuild/SPECS
$ rpmbuild -ba application-firewall.spec
```


