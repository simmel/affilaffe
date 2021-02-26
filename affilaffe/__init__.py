#!/usr/bin/env python3
# pylint: disable=missing-docstring,import-error,invalid-name

import ldap
import ldap3
import ssl


def python_ldap():
    print("python-ldap")
    l = ldap.initialize("ldaps://ldap.su.se")  # noqa: E741

    l.sasl_gssapi_bind_s()
    print("whoami: {}".format(l.whoami_s()))

    result = l.search_s(base="",
                        scope=ldap.SCOPE_SUBTREE,
                        filterstr="(uid=simlu)",
                        attrlist=["eduPersonAffiliation", "displayName"])

    for _dn, entry in result:
        for attribute in entry:
            print("attribute: {} is: {!r}".format(
                attribute,
                # We need to decode the bytes to UTF-8 apparently
                [a.decode("utf-8") for a in entry[attribute]]))


def ldaptre():
    print("ldap3")
    conn = ldap3.Connection(
        server=ldap3.Server('ldap.su.se',
            use_ssl=True,
            tls=ldap3.Tls(
                validate=ssl.CERT_REQUIRED,
                )
            ),
        auto_bind=True,
        authentication=ldap3.SASL,
        sasl_mechanism=ldap3.GSSAPI,
    )
    print("whoami: {}".format(conn.extend.standard.who_am_i()))
    conn.search(search_base='',
                search_scope=ldap3.SUBTREE,
                search_filter='(uid=simlu)',
                attributes=['eduPersonAffiliation', 'displayName'])
    for entry in conn.entries:
        for attribute in entry.entry_attributes:
            print("attribute: {} is: {!r}".format(attribute,
                                                  entry[attribute].values))


def main():
    python_ldap()
    print("")
    ldaptre()


if __name__ == "__main__":
    main()
