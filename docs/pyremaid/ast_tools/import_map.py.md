# ./src/pyremaid/ast_tools/import_map.py

### Imports

  - [ast_tools.get_ast_root_node_for_file](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.get_used_import_list](/docs/pyremaid/ast_tools/__init__.py.md)
  - [files.source.get_source_code_from_file](/docs/pyremaid/files/source.py.md)
  - [files.source.get_import_name_from_path](/docs/pyremaid/files/source.py.md)

---
```mermaid
flowchart TB
  _c68_f69_n1794["AnnAssign"]
  _c68_f69_n1795["Attribute"]
  _c68_f69_n1796["Name"]
  _c68_f69_n1797["Load"]
  _c68_f69_n1798["Store"]
  _c68_f69_n1799["Subscript"]
  _c68_f69_n1800["Name"]
  _c68_f69_n1801["Load"]
  _c68_f69_n1802["Tuple"]
  _c68_f69_n1803["Name"]
  _c68_f69_n1804["Load"]
  _c68_f69_n1805["Subscript"]
  _c68_f69_n1806["Name"]
  _c68_f69_n1807["Load"]
  _c68_f69_n1808["Name"]
  _c68_f69_n1809["Load"]
  _c68_f69_n1810["Load"]
  _c68_f69_n1811["Load"]
  _c68_f69_n1812["Load"]
  _c68_f69_n1813["Dict"]
  _c68_f69_n1814["AnnAssign"]
  _c68_f69_n1815["Attribute"]
  _c68_f69_n1816["Name"]
  _c68_f69_n1817["Load"]
  _c68_f69_n1818["Store"]
  _c68_f69_n1819["Subscript"]
  _c68_f69_n1820["Name"]
  _c68_f69_n1821["Load"]
  _c68_f69_n1822["Tuple"]
  _c68_f69_n1823["Name"]
  _c68_f69_n1824["Load"]
  _c68_f69_n1825["Subscript"]
  _c68_f69_n1826["Name"]
  _c68_f69_n1827["Load"]
  _c68_f69_n1828["Name"]
  _c68_f69_n1829["Load"]
  _c68_f69_n1830["Load"]
  _c68_f69_n1831["Load"]
  _c68_f69_n1832["Load"]
  _c68_f69_n1833["Dict"]
  _c68_f70_n1834["If"]
  _c68_f70_n1835["Compare"]
  _c68_f70_n1836["Name"]
  _c68_f70_n1837["Load"]
  _c68_f70_n1838["NotIn"]
  _c68_f70_n1839["Attribute"]
  _c68_f70_n1840["Name"]
  _c68_f70_n1841["Load"]
  _c68_f70_n1842["Load"]
  _c68_f70_n1843["Assign"]
  _c68_f70_n1844["Subscript"]
  _c68_f70_n1845["Attribute"]
  _c68_f70_n1846["Name"]
  _c68_f70_n1847["Load"]
  _c68_f70_n1848["Load"]
  _c68_f70_n1849["Name"]
  _c68_f70_n1850["Load"]
  _c68_f70_n1851["Store"]
  _c68_f70_n1852["List"]
  _c68_f70_n1853["Load"]
  _c68_f70_n1854["Expr"]
  _c68_f70_n1855["Call"]
  _c68_f70_n1856["Attribute"]
  _c68_f70_n1857["Subscript"]
  _c68_f70_n1858["Attribute"]
  _c68_f70_n1859["Name"]
  _c68_f70_n1860["Load"]
  _c68_f70_n1861["Load"]
  _c68_f70_n1862["Name"]
  _c68_f70_n1863["Load"]
  _c68_f70_n1864["Load"]
  _c68_f70_n1865["Load"]
  _c68_f70_n1866["Name"]
  _c68_f70_n1867["Load"]
  _c68_f70_n1868["If"]
  _c68_f70_n1869["Compare"]
  _c68_f70_n1870["Name"]
  _c68_f70_n1871["Load"]
  _c68_f70_n1872["NotIn"]
  _c68_f70_n1873["Attribute"]
  _c68_f70_n1874["Name"]
  _c68_f70_n1875["Load"]
  _c68_f70_n1876["Load"]
  _c68_f70_n1877["Assign"]
  _c68_f70_n1878["Subscript"]
  _c68_f70_n1879["Attribute"]
  _c68_f70_n1880["Name"]
  _c68_f70_n1881["Load"]
  _c68_f70_n1882["Load"]
  _c68_f70_n1883["Name"]
  _c68_f70_n1884["Load"]
  _c68_f70_n1885["Store"]
  _c68_f70_n1886["List"]
  _c68_f70_n1887["Load"]
  _c68_f70_n1888["Expr"]
  _c68_f70_n1889["Subscript"]
  _c68_f70_n1890["Attribute"]
  _c68_f70_n1891["Subscript"]
  _c68_f70_n1892["Attribute"]
  _c68_f70_n1893["Name"]
  _c68_f70_n1894["Load"]
  _c68_f70_n1895["Load"]
  _c68_f70_n1896["Name"]
  _c68_f70_n1897["Load"]
  _c68_f70_n1898["Load"]
  _c68_f70_n1899["Load"]
  _c68_f70_n1900["Name"]
  _c68_f70_n1901["Load"]
  _c68_f70_n1902["Load"]
  _f71_n1903["Expr"]
  _f71_n1904["Constant"]
  _f71_n1905["Assign"]
  _f71_n1906["Name"]
  _f71_n1907["Store"]
  _f71_n1908["Dict"]
  _f71_l72["in_file"]
  _f71_l72_n1909["Assign"]
  _f71_l72_n1910["Name"]
  _f71_l72_n1911["Store"]
  _f71_l72_n1912["Call"]
  _f71_l72_n1913["Name"]
  _f71_l72_n1914["Load"]
  _f71_l72_n1915["keyword"]
  _f71_l72_n1916["Name"]
  _f71_l72_n1917["Load"]
  _f71_l72_n1918["keyword"]
  _f71_l72_n1919["Name"]
  _f71_l72_n1920["Load"]
  _f71_l72_n1921["Assign"]
  _f71_l72_n1922["Subscript"]
  _f71_l72_n1923["Name"]
  _f71_l72_n1924["Load"]
  _f71_l72_n1925["Name"]
  _f71_l72_n1926["Load"]
  _f71_l72_n1927["Store"]
  _f71_l72_n1928["Name"]
  _f71_l72_n1929["Load"]
  _f71_n1930["Return"]
  _f71_n1931["Name"]
  _f71_n1932["Load"]
  _f73_n1933["Return"]
  _f73_n1934["Subscript"]
  _f73_n1935["Name"]
  _f73_n1936["Load"]
  _f73_n1937["Slice"]
  _f73_n1938["Constant"]
  _f73_n1939["Call"]
  _f73_n1940["Attribute"]
  _f73_n1941["Name"]
  _f73_n1942["Load"]
  _f73_n1943["Load"]
  _f73_n1944["Constant"]
  _f73_n1945["Load"]
  _f74_n1946["Assign"]
  _f74_n1947["Name"]
  _f74_n1948["Store"]
  _f74_n1949["Dict"]
  _f74_l75["in_file"]
  _f74_l75_n1950["If"]
  _f74_l75_n1951["NamedExpr"]
  _f74_l75_n1952["Name"]
  _f74_l75_n1953["Store"]
  _f74_l75_n1954["Call"]
  _f74_l75_n1955["Name"]
  _f74_l75_n1956["Load"]
  _f74_l75_n1957["keyword"]
  _f74_l75_n1958["Name"]
  _f74_l75_n1959["Load"]
  _f74_l75_n1960["If"]
  _f74_l75_n1961["NamedExpr"]
  _f74_l75_n1962["Name"]
  _f74_l75_n1963["Store"]
  _f74_l75_n1964["Call"]
  _f74_l75_n1965["Name"]
  _f74_l75_n1966["Load"]
  _f74_l75_n1967["keyword"]
  _f74_l75_n1968["Name"]
  _f74_l75_n1969["Load"]
  _f74_l75_n1970["keyword"]
  _f74_l75_n1971["Name"]
  _f74_l75_n1972["Load"]
  _f74_l75_l76["used_import"]
  _f74_l75_l76_n1973["Assign"]
  _f74_l75_l76_n1974["Name"]
  _f74_l75_l76_n1975["Store"]
  _f74_l75_l76_n1976["Constant"]
  _f74_l75_l76_n1977["Assign"]
  _f74_l75_l76_n1978["Name"]
  _f74_l75_l76_n1979["Store"]
  _f74_l75_l76_n1980["Call"]
  _f74_l75_l76_n1981["Name"]
  _f74_l75_l76_n1982["Load"]
  _f74_l75_l76_n1983["Name"]
  _f74_l75_l76_n1984["Load"]
  _f74_l75_l76_n1985["If"]
  _f74_l75_l76_n1986["Compare"]
  _f74_l75_l76_n1987["Name"]
  _f74_l75_l76_n1988["Load"]
  _f74_l75_l76_n1989["In"]
  _f74_l75_l76_n1990["Name"]
  _f74_l75_l76_n1991["Load"]
  _f74_l75_l76_n1992["Assign"]
  _f74_l75_l76_n1993["Name"]
  _f74_l75_l76_n1994["Store"]
  _f74_l75_l76_n1995["Subscript"]
  _f74_l75_l76_n1996["Name"]
  _f74_l75_l76_n1997["Load"]
  _f74_l75_l76_n1998["Name"]
  _f74_l75_l76_n1999["Load"]
  _f74_l75_l76_n2000["Load"]
  _f74_l75_l76_n2001["Assign"]
  _f74_l75_l76_n2002["Subscript"]
  _f74_l75_l76_n2003["Name"]
  _f74_l75_l76_n2004["Load"]
  _f74_l75_l76_n2005["Name"]
  _f74_l75_l76_n2006["Load"]
  _f74_l75_l76_n2007["Store"]
  _f74_l75_l76_n2008["Name"]
  _f74_l75_l76_n2009["Load"]
  _f74_n2010["Return"]
  _f74_n2011["Name"]
  _f74_n2012["Load"]
  _f77_n2013["Expr"]
  _f77_n2014["Constant"]
  _f77_n2015["Assign"]
  _f77_n2016["Name"]
  _f77_n2017["Store"]
  _f77_n2018["Call"]
  _f77_n2019["Name"]
  _f77_n2020["Load"]
  _f77_n2021["keyword"]
  _f77_n2022["Name"]
  _f77_n2023["Load"]
  _f77_n2024["keyword"]
  _f77_n2025["Name"]
  _f77_n2026["Load"]
  _f77_n2027["Assign"]
  _f77_n2028["Name"]
  _f77_n2029["Store"]
  _f77_n2030["Call"]
  _f77_n2031["Name"]
  _f77_n2032["Load"]
  _f77_n2033["keyword"]
  _f77_n2034["Name"]
  _f77_n2035["Load"]
  _f77_n2036["keyword"]
  _f77_n2037["Name"]
  _f77_n2038["Load"]
  _f77_n2039["Return"]
  _f77_n2040["Name"]
  _f77_n2041["Load"]

  subgraph ImportMap
    direction TB
    subgraph _c68___init__
      direction TB
      _c68_f69_n1794 --> _c68_f69_n1795
      _c68_f69_n1795 --> _c68_f69_n1796
      _c68_f69_n1796 --> _c68_f69_n1797
      _c68_f69_n1797 --> _c68_f69_n1798
      _c68_f69_n1798 --> _c68_f69_n1799
      _c68_f69_n1799 --> _c68_f69_n1800
      _c68_f69_n1800 --> _c68_f69_n1801
      _c68_f69_n1801 --> _c68_f69_n1802
      _c68_f69_n1802 --> _c68_f69_n1803
      _c68_f69_n1803 --> _c68_f69_n1804
      _c68_f69_n1804 --> _c68_f69_n1805
      _c68_f69_n1805 --> _c68_f69_n1806
      _c68_f69_n1806 --> _c68_f69_n1807
      _c68_f69_n1807 --> _c68_f69_n1808
      _c68_f69_n1808 --> _c68_f69_n1809
      _c68_f69_n1809 --> _c68_f69_n1810
      _c68_f69_n1810 --> _c68_f69_n1811
      _c68_f69_n1811 --> _c68_f69_n1812
      _c68_f69_n1812 --> _c68_f69_n1813
      _c68_f69_n1813 --> _c68_f69_n1814
      _c68_f69_n1814 --> _c68_f69_n1815
      _c68_f69_n1815 --> _c68_f69_n1816
      _c68_f69_n1816 --> _c68_f69_n1817
      _c68_f69_n1817 --> _c68_f69_n1818
      _c68_f69_n1818 --> _c68_f69_n1819
      _c68_f69_n1819 --> _c68_f69_n1820
      _c68_f69_n1820 --> _c68_f69_n1821
      _c68_f69_n1821 --> _c68_f69_n1822
      _c68_f69_n1822 --> _c68_f69_n1823
      _c68_f69_n1823 --> _c68_f69_n1824
      _c68_f69_n1824 --> _c68_f69_n1825
      _c68_f69_n1825 --> _c68_f69_n1826
      _c68_f69_n1826 --> _c68_f69_n1827
      _c68_f69_n1827 --> _c68_f69_n1828
      _c68_f69_n1828 --> _c68_f69_n1829
      _c68_f69_n1829 --> _c68_f69_n1830
      _c68_f69_n1830 --> _c68_f69_n1831
      _c68_f69_n1831 --> _c68_f69_n1832
      _c68_f69_n1832 --> _c68_f69_n1833
    end
    subgraph _c68_add_import
      direction TB
      _c68_f70_n1834 --> _c68_f70_n1835
      _c68_f70_n1835 --> _c68_f70_n1836
      _c68_f70_n1836 --> _c68_f70_n1837
      _c68_f70_n1837 --> _c68_f70_n1838
      _c68_f70_n1838 --> _c68_f70_n1839
      _c68_f70_n1839 --> _c68_f70_n1840
      _c68_f70_n1840 --> _c68_f70_n1841
      _c68_f70_n1841 --> _c68_f70_n1842
      _c68_f70_n1842 --> _c68_f70_n1843
      _c68_f70_n1843 --> _c68_f70_n1844
      _c68_f70_n1844 --> _c68_f70_n1845
      _c68_f70_n1845 --> _c68_f70_n1846
      _c68_f70_n1846 --> _c68_f70_n1847
      _c68_f70_n1847 --> _c68_f70_n1848
      _c68_f70_n1848 --> _c68_f70_n1849
      _c68_f70_n1849 --> _c68_f70_n1850
      _c68_f70_n1850 --> _c68_f70_n1851
      _c68_f70_n1851 --> _c68_f70_n1852
      _c68_f70_n1852 --> _c68_f70_n1853
      _c68_f70_n1853 --> _c68_f70_n1854
      _c68_f70_n1854 --> _c68_f70_n1855
      _c68_f70_n1855 --> _c68_f70_n1856
      _c68_f70_n1856 --> _c68_f70_n1857
      _c68_f70_n1857 --> _c68_f70_n1858
      _c68_f70_n1858 --> _c68_f70_n1859
      _c68_f70_n1859 --> _c68_f70_n1860
      _c68_f70_n1860 --> _c68_f70_n1861
      _c68_f70_n1861 --> _c68_f70_n1862
      _c68_f70_n1862 --> _c68_f70_n1863
      _c68_f70_n1863 --> _c68_f70_n1864
      _c68_f70_n1864 --> _c68_f70_n1865
      _c68_f70_n1865 --> _c68_f70_n1866
      _c68_f70_n1866 --> _c68_f70_n1867
      _c68_f70_n1867 --> _c68_f70_n1868
      _c68_f70_n1868 --> _c68_f70_n1869
      _c68_f70_n1869 --> _c68_f70_n1870
      _c68_f70_n1870 --> _c68_f70_n1871
      _c68_f70_n1871 --> _c68_f70_n1872
      _c68_f70_n1872 --> _c68_f70_n1873
      _c68_f70_n1873 --> _c68_f70_n1874
      _c68_f70_n1874 --> _c68_f70_n1875
      _c68_f70_n1875 --> _c68_f70_n1876
      _c68_f70_n1876 --> _c68_f70_n1877
      _c68_f70_n1877 --> _c68_f70_n1878
      _c68_f70_n1878 --> _c68_f70_n1879
      _c68_f70_n1879 --> _c68_f70_n1880
      _c68_f70_n1880 --> _c68_f70_n1881
      _c68_f70_n1881 --> _c68_f70_n1882
      _c68_f70_n1882 --> _c68_f70_n1883
      _c68_f70_n1883 --> _c68_f70_n1884
      _c68_f70_n1884 --> _c68_f70_n1885
      _c68_f70_n1885 --> _c68_f70_n1886
      _c68_f70_n1886 --> _c68_f70_n1887
      _c68_f70_n1887 --> _c68_f70_n1888
      _c68_f70_n1888 --> _c68_f70_n1889
      _c68_f70_n1889 --> _c68_f70_n1890
      _c68_f70_n1890 --> _c68_f70_n1891
      _c68_f70_n1891 --> _c68_f70_n1892
      _c68_f70_n1892 --> _c68_f70_n1893
      _c68_f70_n1893 --> _c68_f70_n1894
      _c68_f70_n1894 --> _c68_f70_n1895
      _c68_f70_n1895 --> _c68_f70_n1896
      _c68_f70_n1896 --> _c68_f70_n1897
      _c68_f70_n1897 --> _c68_f70_n1898
      _c68_f70_n1898 --> _c68_f70_n1899
      _c68_f70_n1899 --> _c68_f70_n1900
      _c68_f70_n1900 --> _c68_f70_n1901
      _c68_f70_n1901 --> _c68_f70_n1902
    end
  end
  subgraph __get_import_to_file_map
    direction TB
    _f71_n1903 --> _f71_n1904
    _f71_n1904 --> _f71_n1905
    _f71_n1905 --> _f71_n1906
    _f71_n1906 --> _f71_n1907
    _f71_n1907 --> _f71_n1908
    _f71_n1908 --> _f71_l72
    %% loop in_file
      _f71_l72_n1909 --> _f71_l72_n1910
      _f71_l72_n1910 --> _f71_l72_n1911
      _f71_l72_n1911 --> _f71_l72_n1912
      _f71_l72_n1912 --> _f71_l72_n1913
      _f71_l72_n1913 --> _f71_l72_n1914
      _f71_l72_n1914 --> _f71_l72_n1915
      _f71_l72_n1915 --> _f71_l72_n1916
      _f71_l72_n1916 --> _f71_l72_n1917
      _f71_l72_n1917 --> _f71_l72_n1918
      _f71_l72_n1918 --> _f71_l72_n1919
      _f71_l72_n1919 --> _f71_l72_n1920
      _f71_l72_n1920 --> _f71_l72_n1921
      _f71_l72_n1921 --> _f71_l72_n1922
      _f71_l72_n1922 --> _f71_l72_n1923
      _f71_l72_n1923 --> _f71_l72_n1924
      _f71_l72_n1924 --> _f71_l72_n1925
      _f71_l72_n1925 --> _f71_l72_n1926
      _f71_l72_n1926 --> _f71_l72_n1927
      _f71_l72_n1927 --> _f71_l72_n1928
      _f71_l72_n1928 --> _f71_l72_n1929
    %% end in_file
    _f71_l72_n1929 --> _f71_l72_n1909
    _f71_l72_n1909 --> _f71_n1930
    _f71_n1930 --> _f71_n1931
    _f71_n1931 --> _f71_n1932
  end
  subgraph __get_parent_import
    direction TB
    _f73_n1933 --> _f73_n1934
    _f73_n1934 --> _f73_n1935
    _f73_n1935 --> _f73_n1936
    _f73_n1936 --> _f73_n1937
    _f73_n1937 --> _f73_n1938
    _f73_n1938 --> _f73_n1939
    _f73_n1939 --> _f73_n1940
    _f73_n1940 --> _f73_n1941
    _f73_n1941 --> _f73_n1942
    _f73_n1942 --> _f73_n1943
    _f73_n1943 --> _f73_n1944
    _f73_n1944 --> _f73_n1945
  end
  subgraph __create_import_table
    direction TB
    _f74_n1946 --> _f74_n1947
    _f74_n1947 --> _f74_n1948
    _f74_n1948 --> _f74_n1949
    _f74_n1949 --> _f74_l75
    %% loop in_file
      _f74_l75_n1950 --> _f74_l75_n1951
      _f74_l75_n1951 --> _f74_l75_n1952
      _f74_l75_n1952 --> _f74_l75_n1953
      _f74_l75_n1953 --> _f74_l75_n1954
      _f74_l75_n1954 --> _f74_l75_n1955
      _f74_l75_n1955 --> _f74_l75_n1956
      _f74_l75_n1956 --> _f74_l75_n1957
      _f74_l75_n1957 --> _f74_l75_n1958
      _f74_l75_n1958 --> _f74_l75_n1959
      _f74_l75_n1959 --> _f74_l75_n1960
      _f74_l75_n1960 --> _f74_l75_n1961
      _f74_l75_n1961 --> _f74_l75_n1962
      _f74_l75_n1962 --> _f74_l75_n1963
      _f74_l75_n1963 --> _f74_l75_n1964
      _f74_l75_n1964 --> _f74_l75_n1965
      _f74_l75_n1965 --> _f74_l75_n1966
      _f74_l75_n1966 --> _f74_l75_n1967
      _f74_l75_n1967 --> _f74_l75_n1968
      _f74_l75_n1968 --> _f74_l75_n1969
      _f74_l75_n1969 --> _f74_l75_n1970
      _f74_l75_n1970 --> _f74_l75_n1971
      _f74_l75_n1971 --> _f74_l75_n1972
      _f74_l75_n1972 --> _f74_l75_l76
      %% loop used_import
        _f74_l75_l76_n1973 --> _f74_l75_l76_n1974
        _f74_l75_l76_n1974 --> _f74_l75_l76_n1975
        _f74_l75_l76_n1975 --> _f74_l75_l76_n1976
        _f74_l75_l76_n1976 --> _f74_l75_l76_n1977
        _f74_l75_l76_n1977 --> _f74_l75_l76_n1978
        _f74_l75_l76_n1978 --> _f74_l75_l76_n1979
        _f74_l75_l76_n1979 --> _f74_l75_l76_n1980
        _f74_l75_l76_n1980 --> _f74_l75_l76_n1981
        _f74_l75_l76_n1981 --> _f74_l75_l76_n1982
        _f74_l75_l76_n1982 --> _f74_l75_l76_n1983
        _f74_l75_l76_n1983 --> _f74_l75_l76_n1984
        _f74_l75_l76_n1984 --> _f74_l75_l76_n1985
        _f74_l75_l76_n1985 --> _f74_l75_l76_n1986
        _f74_l75_l76_n1986 --> _f74_l75_l76_n1987
        _f74_l75_l76_n1987 --> _f74_l75_l76_n1988
        _f74_l75_l76_n1988 --> _f74_l75_l76_n1989
        _f74_l75_l76_n1989 --> _f74_l75_l76_n1990
        _f74_l75_l76_n1990 --> _f74_l75_l76_n1991
        _f74_l75_l76_n1991 --> _f74_l75_l76_n1992
        _f74_l75_l76_n1992 --> _f74_l75_l76_n1993
        _f74_l75_l76_n1993 --> _f74_l75_l76_n1994
        _f74_l75_l76_n1994 --> _f74_l75_l76_n1995
        _f74_l75_l76_n1995 --> _f74_l75_l76_n1996
        _f74_l75_l76_n1996 --> _f74_l75_l76_n1997
        _f74_l75_l76_n1997 --> _f74_l75_l76_n1998
        _f74_l75_l76_n1998 --> _f74_l75_l76_n1999
        _f74_l75_l76_n1999 --> _f74_l75_l76_n2000
        _f74_l75_l76_n2000 --> _f74_l75_l76_n2001
        _f74_l75_l76_n2001 --> _f74_l75_l76_n2002
        _f74_l75_l76_n2002 --> _f74_l75_l76_n2003
        _f74_l75_l76_n2003 --> _f74_l75_l76_n2004
        _f74_l75_l76_n2004 --> _f74_l75_l76_n2005
        _f74_l75_l76_n2005 --> _f74_l75_l76_n2006
        _f74_l75_l76_n2006 --> _f74_l75_l76_n2007
        _f74_l75_l76_n2007 --> _f74_l75_l76_n2008
        _f74_l75_l76_n2008 --> _f74_l75_l76_n2009
      %% end used_import
      _f74_l75_l76_n2009 --> _f74_l75_l76_n1973
    %% end in_file
    _f74_l75_l76_n1973 --> _f74_l75_n1950
    _f74_l75_n1950 --> _f74_n2010
    _f74_n2010 --> _f74_n2011
    _f74_n2011 --> _f74_n2012
  end
  subgraph _get_all_imports_from_files
    direction TB
    _f77_n2013 --> _f77_n2014
    _f77_n2014 --> _f77_n2015
    _f77_n2015 --> _f77_n2016
    _f77_n2016 --> _f77_n2017
    _f77_n2017 --> _f77_n2018
    _f77_n2018 --> _f77_n2019
    _f77_n2019 --> _f77_n2020
    _f77_n2020 --> _f77_n2021
    _f77_n2021 --> _f77_n2022
    _f77_n2022 --> _f77_n2023
    _f77_n2023 --> _f77_n2024
    _f77_n2024 --> _f77_n2025
    _f77_n2025 --> _f77_n2026
    _f77_n2026 --> _f77_n2027
    _f77_n2027 --> _f77_n2028
    _f77_n2028 --> _f77_n2029
    _f77_n2029 --> _f77_n2030
    _f77_n2030 --> _f77_n2031
    _f77_n2031 --> _f77_n2032
    _f77_n2032 --> _f77_n2033
    _f77_n2033 --> _f77_n2034
    _f77_n2034 --> _f77_n2035
    _f77_n2035 --> _f77_n2036
    _f77_n2036 --> _f77_n2037
    _f77_n2037 --> _f77_n2038
    _f77_n2038 --> _f77_n2039
    _f77_n2039 --> _f77_n2040
    _f77_n2040 --> _f77_n2041
  end

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='ast_tools',
      names=[
        alias(name='get_ast_root_node_for_file'),
        alias(name='get_used_import_list')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=70),
    ImportFrom(
      module='files.source',
      names=[
        alias(name='get_source_code_from_file'),
        alias(name='get_import_name_from_path')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=2,
      end_col_offset=77),
    ClassDef(
      name='ImportMap',
      bases=[],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=7,
                col_offset=17,
                end_lineno=7,
                end_col_offset=21)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=8,
                  col_offset=8,
                  end_lineno=8,
                  end_col_offset=12),
                attr='import_to',
                ctx=Store(),
                lineno=8,
                col_offset=8,
                end_lineno=8,
                end_col_offset=22),
              annotation=Subscript(
                value=Name(
                  id='dict',
                  ctx=Load(),
                  lineno=8,
                  col_offset=25,
                  end_lineno=8,
                  end_col_offset=29),
                slice=Tuple(
                  elts=[
                    Name(
                      id='str',
                      ctx=Load(),
                      lineno=8,
                      col_offset=30,
                      end_lineno=8,
                      end_col_offset=33),
                    Subscript(
                      value=Name(
                        id='list',
                        ctx=Load(),
                        lineno=8,
                        col_offset=35,
                        end_lineno=8,
                        end_col_offset=39),
                      slice=Name(
                        id='str',
                        ctx=Load(),
                        lineno=8,
                        col_offset=40,
                        end_lineno=8,
                        end_col_offset=43),
                      ctx=Load(),
                      lineno=8,
                      col_offset=35,
                      end_lineno=8,
                      end_col_offset=44)],
                  ctx=Load(),
                  lineno=8,
                  col_offset=30,
                  end_lineno=8,
                  end_col_offset=44),
                ctx=Load(),
                lineno=8,
                col_offset=25,
                end_lineno=8,
                end_col_offset=45),
              value=Dict(
                keys=[],
                values=[],
                lineno=8,
                col_offset=48,
                end_lineno=8,
                end_col_offset=50),
              simple=0,
              lineno=8,
              col_offset=8,
              end_lineno=8,
              end_col_offset=50),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=9,
                  col_offset=8,
                  end_lineno=9,
                  end_col_offset=12),
                attr='import_from',
                ctx=Store(),
                lineno=9,
                col_offset=8,
                end_lineno=9,
                end_col_offset=24),
              annotation=Subscript(
                value=Name(
                  id='dict',
                  ctx=Load(),
                  lineno=9,
                  col_offset=27,
                  end_lineno=9,
                  end_col_offset=31),
                slice=Tuple(
                  elts=[
                    Name(
                      id='str',
                      ctx=Load(),
                      lineno=9,
                      col_offset=32,
                      end_lineno=9,
                      end_col_offset=35),
                    Subscript(
                      value=Name(
                        id='list',
                        ctx=Load(),
                        lineno=9,
                        col_offset=37,
                        end_lineno=9,
                        end_col_offset=41),
                      slice=Name(
                        id='str',
                        ctx=Load(),
                        lineno=9,
                        col_offset=42,
                        end_lineno=9,
                        end_col_offset=45),
                      ctx=Load(),
                      lineno=9,
                      col_offset=37,
                      end_lineno=9,
                      end_col_offset=46)],
                  ctx=Load(),
                  lineno=9,
                  col_offset=32,
                  end_lineno=9,
                  end_col_offset=46),
                ctx=Load(),
                lineno=9,
                col_offset=27,
                end_lineno=9,
                end_col_offset=47),
              value=Dict(
                keys=[],
                values=[],
                lineno=9,
                col_offset=50,
                end_lineno=9,
                end_col_offset=52),
              simple=0,
              lineno=9,
              col_offset=8,
              end_lineno=9,
              end_col_offset=52)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=7,
            col_offset=26,
            end_lineno=7,
            end_col_offset=30),
          lineno=7,
          col_offset=4,
          end_lineno=9,
          end_col_offset=52),
        FunctionDef(
          name='add_import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=12,
                col_offset=19,
                end_lineno=12,
                end_col_offset=23),
              arg(
                arg='from_',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=12,
                  col_offset=32,
                  end_lineno=12,
                  end_col_offset=35),
                lineno=12,
                col_offset=25,
                end_lineno=12,
                end_col_offset=35),
              arg(
                arg='to',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=12,
                  col_offset=41,
                  end_lineno=12,
                  end_col_offset=44),
                lineno=12,
                col_offset=37,
                end_lineno=12,
                end_col_offset=44)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            If(
              test=Compare(
                left=Name(
                  id='from_',
                  ctx=Load(),
                  lineno=13,
                  col_offset=11,
                  end_lineno=13,
                  end_col_offset=16),
                ops=[
                  NotIn()],
                comparators=[
                  Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=13,
                      col_offset=24,
                      end_lineno=13,
                      end_col_offset=28),
                    attr='import_to',
                    ctx=Load(),
                    lineno=13,
                    col_offset=24,
                    end_lineno=13,
                    end_col_offset=38)],
                lineno=13,
                col_offset=11,
                end_lineno=13,
                end_col_offset=38),
              body=[
                Assign(
                  targets=[
                    Subscript(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=14,
                          col_offset=12,
                          end_lineno=14,
                          end_col_offset=16),
                        attr='import_to',
                        ctx=Load(),
                        lineno=14,
                        col_offset=12,
                        end_lineno=14,
                        end_col_offset=26),
                      slice=Name(
                        id='from_',
                        ctx=Load(),
                        lineno=14,
                        col_offset=27,
                        end_lineno=14,
                        end_col_offset=32),
                      ctx=Store(),
                      lineno=14,
                      col_offset=12,
                      end_lineno=14,
                      end_col_offset=33)],
                  value=List(
                    elts=[],
                    ctx=Load(),
                    lineno=14,
                    col_offset=36,
                    end_lineno=14,
                    end_col_offset=38),
                  lineno=14,
                  col_offset=12,
                  end_lineno=14,
                  end_col_offset=38)],
              orelse=[],
              lineno=13,
              col_offset=8,
              end_lineno=14,
              end_col_offset=38),
            Expr(
              value=Call(
                func=Attribute(
                  value=Subscript(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=15,
                        col_offset=8,
                        end_lineno=15,
                        end_col_offset=12),
                      attr='import_to',
                      ctx=Load(),
                      lineno=15,
                      col_offset=8,
                      end_lineno=15,
                      end_col_offset=22),
                    slice=Name(
                      id='from_',
                      ctx=Load(),
                      lineno=15,
                      col_offset=23,
                      end_lineno=15,
                      end_col_offset=28),
                    ctx=Load(),
                    lineno=15,
                    col_offset=8,
                    end_lineno=15,
                    end_col_offset=29),
                  attr='append',
                  ctx=Load(),
                  lineno=15,
                  col_offset=8,
                  end_lineno=15,
                  end_col_offset=36),
                args=[
                  Name(
                    id='to',
                    ctx=Load(),
                    lineno=15,
                    col_offset=37,
                    end_lineno=15,
                    end_col_offset=39)],
                keywords=[],
                lineno=15,
                col_offset=8,
                end_lineno=15,
                end_col_offset=40),
              lineno=15,
              col_offset=8,
              end_lineno=15,
              end_col_offset=40),
            If(
              test=Compare(
                left=Name(
                  id='to',
                  ctx=Load(),
                  lineno=17,
                  col_offset=11,
                  end_lineno=17,
                  end_col_offset=13),
                ops=[
                  NotIn()],
                comparators=[
                  Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=17,
                      col_offset=21,
                      end_lineno=17,
                      end_col_offset=25),
                    attr='import_from',
                    ctx=Load(),
                    lineno=17,
                    col_offset=21,
                    end_lineno=17,
                    end_col_offset=37)],
                lineno=17,
                col_offset=11,
                end_lineno=17,
                end_col_offset=37),
              body=[
                Assign(
                  targets=[
                    Subscript(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=18,
                          col_offset=12,
                          end_lineno=18,
                          end_col_offset=16),
                        attr='import_from',
                        ctx=Load(),
                        lineno=18,
                        col_offset=12,
                        end_lineno=18,
                        end_col_offset=28),
                      slice=Name(
                        id='to',
                        ctx=Load(),
                        lineno=18,
                        col_offset=29,
                        end_lineno=18,
                        end_col_offset=31),
                      ctx=Store(),
                      lineno=18,
                      col_offset=12,
                      end_lineno=18,
                      end_col_offset=32)],
                  value=List(
                    elts=[],
                    ctx=Load(),
                    lineno=18,
                    col_offset=35,
                    end_lineno=18,
                    end_col_offset=37),
                  lineno=18,
                  col_offset=12,
                  end_lineno=18,
                  end_col_offset=37)],
              orelse=[],
              lineno=17,
              col_offset=8,
              end_lineno=18,
              end_col_offset=37),
            Expr(
              value=Subscript(
                value=Attribute(
                  value=Subscript(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=19,
                        col_offset=8,
                        end_lineno=19,
                        end_col_offset=12),
                      attr='import_from',
                      ctx=Load(),
                      lineno=19,
                      col_offset=8,
                      end_lineno=19,
                      end_col_offset=24),
                    slice=Name(
                      id='to',
                      ctx=Load(),
                      lineno=19,
                      col_offset=25,
                      end_lineno=19,
                      end_col_offset=27),
                    ctx=Load(),
                    lineno=19,
                    col_offset=8,
                    end_lineno=19,
                    end_col_offset=28),
                  attr='append',
                  ctx=Load(),
                  lineno=19,
                  col_offset=8,
                  end_lineno=19,
                  end_col_offset=35),
                slice=Name(
                  id='from_',
                  ctx=Load(),
                  lineno=19,
                  col_offset=36,
                  end_lineno=19,
                  end_col_offset=41),
                ctx=Load(),
                lineno=19,
                col_offset=8,
                end_lineno=19,
                end_col_offset=42),
              lineno=19,
              col_offset=8,
              end_lineno=19,
              end_col_offset=42)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=12,
            col_offset=49,
            end_lineno=12,
            end_col_offset=53),
          lineno=12,
          col_offset=4,
          end_lineno=19,
          end_col_offset=42)],
      decorator_list=[],
      lineno=5,
      col_offset=0,
      end_lineno=19,
      end_col_offset=42),
    FunctionDef(
      name='_get_import_to_file_map',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=40,
              end_lineno=22,
              end_col_offset=43),
            lineno=22,
            col_offset=28,
            end_lineno=22,
            end_col_offset=43),
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=22,
                col_offset=59,
                end_lineno=22,
                end_col_offset=63),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=22,
                col_offset=64,
                end_lineno=22,
                end_col_offset=67),
              ctx=Load(),
              lineno=22,
              col_offset=59,
              end_lineno=22,
              end_col_offset=68),
            lineno=22,
            col_offset=45,
            end_lineno=22,
            end_col_offset=68)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Constant(
            value=' Create a mapping of import paths to filenames first ',
            lineno=23,
            col_offset=4,
            end_lineno=23,
            end_col_offset=63),
          lineno=23,
          col_offset=4,
          end_lineno=23,
          end_col_offset=63),
        Assign(
          targets=[
            Name(
              id='import_to_file_map',
              ctx=Store(),
              lineno=24,
              col_offset=4,
              end_lineno=24,
              end_col_offset=22)],
          value=Dict(
            keys=[],
            values=[],
            lineno=24,
            col_offset=25,
            end_lineno=24,
            end_col_offset=27),
          lineno=24,
          col_offset=4,
          end_lineno=24,
          end_col_offset=27),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=26,
            col_offset=8,
            end_lineno=26,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=26,
            col_offset=19,
            end_lineno=26,
            end_col_offset=31),
          body=[
            Assign(
              targets=[
                Name(
                  id='import_name',
                  ctx=Store(),
                  lineno=27,
                  col_offset=8,
                  end_lineno=27,
                  end_col_offset=19)],
              value=Call(
                func=Name(
                  id='get_import_name_from_path',
                  ctx=Load(),
                  lineno=27,
                  col_offset=22,
                  end_lineno=27,
                  end_col_offset=47),
                args=[],
                keywords=[
                  keyword(
                    arg='input_path',
                    value=Name(
                      id='input_path',
                      ctx=Load(),
                      lineno=28,
                      col_offset=23,
                      end_lineno=28,
                      end_col_offset=33),
                    lineno=28,
                    col_offset=12,
                    end_lineno=28,
                    end_col_offset=33),
                  keyword(
                    arg='input_file',
                    value=Name(
                      id='in_file',
                      ctx=Load(),
                      lineno=28,
                      col_offset=46,
                      end_lineno=28,
                      end_col_offset=53),
                    lineno=28,
                    col_offset=35,
                    end_lineno=28,
                    end_col_offset=53)],
                lineno=27,
                col_offset=22,
                end_lineno=29,
                end_col_offset=9),
              lineno=27,
              col_offset=8,
              end_lineno=29,
              end_col_offset=9),
            Assign(
              targets=[
                Subscript(
                  value=Name(
                    id='import_to_file_map',
                    ctx=Load(),
                    lineno=30,
                    col_offset=8,
                    end_lineno=30,
                    end_col_offset=26),
                  slice=Name(
                    id='import_name',
                    ctx=Load(),
                    lineno=30,
                    col_offset=27,
                    end_lineno=30,
                    end_col_offset=38),
                  ctx=Store(),
                  lineno=30,
                  col_offset=8,
                  end_lineno=30,
                  end_col_offset=39)],
              value=Name(
                id='in_file',
                ctx=Load(),
                lineno=30,
                col_offset=42,
                end_lineno=30,
                end_col_offset=49),
              lineno=30,
              col_offset=8,
              end_lineno=30,
              end_col_offset=49)],
          orelse=[],
          lineno=26,
          col_offset=4,
          end_lineno=30,
          end_col_offset=49),
        Return(
          value=Name(
            id='import_to_file_map',
            ctx=Load(),
            lineno=32,
            col_offset=11,
            end_lineno=32,
            end_col_offset=29),
          lineno=32,
          col_offset=4,
          end_lineno=32,
          end_col_offset=29)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='dict',
          ctx=Load(),
          lineno=22,
          col_offset=73,
          end_lineno=22,
          end_col_offset=77),
        slice=Tuple(
          elts=[
            Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=78,
              end_lineno=22,
              end_col_offset=81),
            Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=83,
              end_lineno=22,
              end_col_offset=86)],
          ctx=Load(),
          lineno=22,
          col_offset=78,
          end_lineno=22,
          end_col_offset=86),
        ctx=Load(),
        lineno=22,
        col_offset=73,
        end_lineno=22,
        end_col_offset=87),
      lineno=22,
      col_offset=0,
      end_lineno=32,
      end_col_offset=29),
    FunctionDef(
      name='_get_parent_import',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='import_name',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=35,
              col_offset=36,
              end_lineno=35,
              end_col_offset=39),
            lineno=35,
            col_offset=23,
            end_lineno=35,
            end_col_offset=39)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Subscript(
            value=Name(
              id='import_name',
              ctx=Load(),
              lineno=36,
              col_offset=11,
              end_lineno=36,
              end_col_offset=22),
            slice=Slice(
              lower=Constant(
                value=0,
                lineno=36,
                col_offset=23,
                end_lineno=36,
                end_col_offset=24),
              upper=Call(
                func=Attribute(
                  value=Name(
                    id='import_name',
                    ctx=Load(),
                    lineno=36,
                    col_offset=26,
                    end_lineno=36,
                    end_col_offset=37),
                  attr='rfind',
                  ctx=Load(),
                  lineno=36,
                  col_offset=26,
                  end_lineno=36,
                  end_col_offset=43),
                args=[
                  Constant(
                    value='.',
                    lineno=36,
                    col_offset=44,
                    end_lineno=36,
                    end_col_offset=47)],
                keywords=[],
                lineno=36,
                col_offset=26,
                end_lineno=36,
                end_col_offset=48),
              lineno=36,
              col_offset=23,
              end_lineno=36,
              end_col_offset=48),
            ctx=Load(),
            lineno=36,
            col_offset=11,
            end_lineno=36,
            end_col_offset=49),
          lineno=36,
          col_offset=4,
          end_lineno=36,
          end_col_offset=49)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=35,
        col_offset=44,
        end_lineno=35,
        end_col_offset=47),
      lineno=35,
      col_offset=0,
      end_lineno=36,
      end_col_offset=49),
    FunctionDef(
      name='_create_import_table',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=40,
                col_offset=18,
                end_lineno=40,
                end_col_offset=22),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=40,
                col_offset=23,
                end_lineno=40,
                end_col_offset=26),
              ctx=Load(),
              lineno=40,
              col_offset=18,
              end_lineno=40,
              end_col_offset=27),
            lineno=40,
            col_offset=4,
            end_lineno=40,
            end_col_offset=27),
          arg(
            arg='import_to_file_map',
            annotation=Subscript(
              value=Name(
                id='dict',
                ctx=Load(),
                lineno=41,
                col_offset=24,
                end_lineno=41,
                end_col_offset=28),
              slice=Tuple(
                elts=[
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=41,
                    col_offset=29,
                    end_lineno=41,
                    end_col_offset=32),
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=41,
                    col_offset=34,
                    end_lineno=41,
                    end_col_offset=37)],
                ctx=Load(),
                lineno=41,
                col_offset=29,
                end_lineno=41,
                end_col_offset=37),
              ctx=Load(),
              lineno=41,
              col_offset=24,
              end_lineno=41,
              end_col_offset=38),
            lineno=41,
            col_offset=4,
            end_lineno=41,
            end_col_offset=38)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='all_imports_list',
              ctx=Store(),
              lineno=44,
              col_offset=4,
              end_lineno=44,
              end_col_offset=20)],
          value=Dict(
            keys=[],
            values=[],
            lineno=44,
            col_offset=23,
            end_lineno=44,
            end_col_offset=25),
          lineno=44,
          col_offset=4,
          end_lineno=44,
          end_col_offset=25),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=46,
            col_offset=8,
            end_lineno=46,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=46,
            col_offset=19,
            end_lineno=46,
            end_col_offset=31),
          body=[
            If(
              test=NamedExpr(
                target=Name(
                  id='source_code',
                  ctx=Store(),
                  lineno=47,
                  col_offset=11,
                  end_lineno=47,
                  end_col_offset=22),
                value=Call(
                  func=Name(
                    id='get_source_code_from_file',
                    ctx=Load(),
                    lineno=47,
                    col_offset=26,
                    end_lineno=47,
                    end_col_offset=51),
                  args=[],
                  keywords=[
                    keyword(
                      arg='input_file',
                      value=Name(
                        id='in_file',
                        ctx=Load(),
                        lineno=47,
                        col_offset=63,
                        end_lineno=47,
                        end_col_offset=70),
                      lineno=47,
                      col_offset=52,
                      end_lineno=47,
                      end_col_offset=70)],
                  lineno=47,
                  col_offset=26,
                  end_lineno=47,
                  end_col_offset=71),
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=71),
              body=[
                If(
                  test=NamedExpr(
                    target=Name(
                      id='ast_node',
                      ctx=Store(),
                      lineno=48,
                      col_offset=15,
                      end_lineno=48,
                      end_col_offset=23),
                    value=Call(
                      func=Name(
                        id='get_ast_root_node_for_file',
                        ctx=Load(),
                        lineno=48,
                        col_offset=27,
                        end_lineno=48,
                        end_col_offset=53),
                      args=[],
                      keywords=[
                        keyword(
                          arg='source_code',
                          value=Name(
                            id='source_code',
                            ctx=Load(),
                            lineno=49,
                            col_offset=28,
                            end_lineno=49,
                            end_col_offset=39),
                          lineno=49,
                          col_offset=16,
                          end_lineno=49,
                          end_col_offset=39),
                        keyword(
                          arg='input_file',
                          value=Name(
                            id='in_file',
                            ctx=Load(),
                            lineno=50,
                            col_offset=27,
                            end_lineno=50,
                            end_col_offset=34),
                          lineno=50,
                          col_offset=16,
                          end_lineno=50,
                          end_col_offset=34)],
                      lineno=48,
                      col_offset=27,
                      end_lineno=51,
                      end_col_offset=13),
                    lineno=48,
                    col_offset=15,
                    end_lineno=51,
                    end_col_offset=13),
                  body=[
                    For(
                      target=Name(
                        id='used_import',
                        ctx=Store(),
                        lineno=52,
                        col_offset=20,
                        end_lineno=52,
                        end_col_offset=31),
                      iter=Call(
                        func=Name(
                          id='get_used_import_list',
                          ctx=Load(),
                          lineno=52,
                          col_offset=35,
                          end_lineno=52,
                          end_col_offset=55),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=52,
                              col_offset=65,
                              end_lineno=52,
                              end_col_offset=73),
                            lineno=52,
                            col_offset=56,
                            end_lineno=52,
                            end_col_offset=73)],
                        lineno=52,
                        col_offset=35,
                        end_lineno=52,
                        end_col_offset=74),
                      body=[
                        Assign(
                          targets=[
                            Name(
                              id='known_file',
                              ctx=Store(),
                              lineno=53,
                              col_offset=20,
                              end_lineno=53,
                              end_col_offset=30)],
                          value=Constant(
                            value='',
                            lineno=53,
                            col_offset=33,
                            end_lineno=53,
                            end_col_offset=35),
                          lineno=53,
                          col_offset=20,
                          end_lineno=53,
                          end_col_offset=35),
                        Assign(
                          targets=[
                            Name(
                              id='parent_import',
                              ctx=Store(),
                              lineno=54,
                              col_offset=20,
                              end_lineno=54,
                              end_col_offset=33)],
                          value=Call(
                            func=Name(
                              id='_get_parent_import',
                              ctx=Load(),
                              lineno=54,
                              col_offset=36,
                              end_lineno=54,
                              end_col_offset=54),
                            args=[
                              Name(
                                id='used_import',
                                ctx=Load(),
                                lineno=54,
                                col_offset=55,
                                end_lineno=54,
                                end_col_offset=66)],
                            keywords=[],
                            lineno=54,
                            col_offset=36,
                            end_lineno=54,
                            end_col_offset=67),
                          lineno=54,
                          col_offset=20,
                          end_lineno=54,
                          end_col_offset=67),
                        If(
                          test=Compare(
                            left=Name(
                              id='parent_import',
                              ctx=Load(),
                              lineno=55,
                              col_offset=23,
                              end_lineno=55,
                              end_col_offset=36),
                            ops=[
                              In()],
                            comparators=[
                              Name(
                                id='import_to_file_map',
                                ctx=Load(),
                                lineno=55,
                                col_offset=40,
                                end_lineno=55,
                                end_col_offset=58)],
                            lineno=55,
                            col_offset=23,
                            end_lineno=55,
                            end_col_offset=58),
                          body=[
                            Assign(
                              targets=[
                                Name(
                                  id='known_file',
                                  ctx=Store(),
                                  lineno=56,
                                  col_offset=24,
                                  end_lineno=56,
                                  end_col_offset=34)],
                              value=Subscript(
                                value=Name(
                                  id='import_to_file_map',
                                  ctx=Load(),
                                  lineno=56,
                                  col_offset=37,
                                  end_lineno=56,
                                  end_col_offset=55),
                                slice=Name(
                                  id='parent_import',
                                  ctx=Load(),
                                  lineno=56,
                                  col_offset=56,
                                  end_lineno=56,
                                  end_col_offset=69),
                                ctx=Load(),
                                lineno=56,
                                col_offset=37,
                                end_lineno=56,
                                end_col_offset=70),
                              lineno=56,
                              col_offset=24,
                              end_lineno=56,
                              end_col_offset=70)],
                          orelse=[],
                          lineno=55,
                          col_offset=20,
                          end_lineno=56,
                          end_col_offset=70),
                        Assign(
                          targets=[
                            Subscript(
                              value=Name(
                                id='all_imports_list',
                                ctx=Load(),
                                lineno=57,
                                col_offset=20,
                                end_lineno=57,
                                end_col_offset=36),
                              slice=Name(
                                id='used_import',
                                ctx=Load(),
                                lineno=57,
                                col_offset=37,
                                end_lineno=57,
                                end_col_offset=48),
                              ctx=Store(),
                              lineno=57,
                              col_offset=20,
                              end_lineno=57,
                              end_col_offset=49)],
                          value=Name(
                            id='known_file',
                            ctx=Load(),
                            lineno=57,
                            col_offset=52,
                            end_lineno=57,
                            end_col_offset=62),
                          lineno=57,
                          col_offset=20,
                          end_lineno=57,
                          end_col_offset=62)],
                      orelse=[],
                      lineno=52,
                      col_offset=16,
                      end_lineno=57,
                      end_col_offset=62)],
                  orelse=[],
                  lineno=48,
                  col_offset=12,
                  end_lineno=57,
                  end_col_offset=62)],
              orelse=[],
              lineno=47,
              col_offset=8,
              end_lineno=57,
              end_col_offset=62)],
          orelse=[],
          lineno=46,
          col_offset=4,
          end_lineno=57,
          end_col_offset=62),
        Return(
          value=Name(
            id='all_imports_list',
            ctx=Load(),
            lineno=59,
            col_offset=11,
            end_lineno=59,
            end_col_offset=27),
          lineno=59,
          col_offset=4,
          end_lineno=59,
          end_col_offset=27)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='dict',
          ctx=Load(),
          lineno=42,
          col_offset=5,
          end_lineno=42,
          end_col_offset=9),
        slice=Tuple(
          elts=[
            Name(
              id='str',
              ctx=Load(),
              lineno=42,
              col_offset=10,
              end_lineno=42,
              end_col_offset=13),
            Name(
              id='str',
              ctx=Load(),
              lineno=42,
              col_offset=15,
              end_lineno=42,
              end_col_offset=18)],
          ctx=Load(),
          lineno=42,
          col_offset=10,
          end_lineno=42,
          end_col_offset=18),
        ctx=Load(),
        lineno=42,
        col_offset=5,
        end_lineno=42,
        end_col_offset=19),
      lineno=39,
      col_offset=0,
      end_lineno=59,
      end_col_offset=27),
    FunctionDef(
      name='get_all_imports_from_files',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=62,
              col_offset=43,
              end_lineno=62,
              end_col_offset=46),
            lineno=62,
            col_offset=31,
            end_lineno=62,
            end_col_offset=46),
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=62,
                col_offset=62,
                end_lineno=62,
                end_col_offset=66),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=62,
                col_offset=67,
                end_lineno=62,
                end_col_offset=70),
              ctx=Load(),
              lineno=62,
              col_offset=62,
              end_lineno=62,
              end_col_offset=71),
            lineno=62,
            col_offset=48,
            end_lineno=62,
            end_col_offset=71)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Constant(
            value="\n    This is kind of expensive for what it does\n    It's tricky not to require multiple passes to achieve what is being done here\n    ",
            lineno=63,
            col_offset=4,
            end_lineno=66,
            end_col_offset=7),
          lineno=63,
          col_offset=4,
          end_lineno=66,
          end_col_offset=7),
        Assign(
          targets=[
            Name(
              id='import_to_file_map',
              ctx=Store(),
              lineno=68,
              col_offset=4,
              end_lineno=68,
              end_col_offset=22)],
          value=Call(
            func=Name(
              id='_get_import_to_file_map',
              ctx=Load(),
              lineno=68,
              col_offset=25,
              end_lineno=68,
              end_col_offset=48),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=69,
                  col_offset=19,
                  end_lineno=69,
                  end_col_offset=29),
                lineno=69,
                col_offset=8,
                end_lineno=69,
                end_col_offset=29),
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=69,
                  col_offset=44,
                  end_lineno=69,
                  end_col_offset=56),
                lineno=69,
                col_offset=31,
                end_lineno=69,
                end_col_offset=56)],
            lineno=68,
            col_offset=25,
            end_lineno=70,
            end_col_offset=5),
          lineno=68,
          col_offset=4,
          end_lineno=70,
          end_col_offset=5),
        Assign(
          targets=[
            Name(
              id='all_imports_list',
              ctx=Store(),
              lineno=72,
              col_offset=4,
              end_lineno=72,
              end_col_offset=20)],
          value=Call(
            func=Name(
              id='_create_import_table',
              ctx=Load(),
              lineno=72,
              col_offset=23,
              end_lineno=72,
              end_col_offset=43),
            args=[],
            keywords=[
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=73,
                  col_offset=21,
                  end_lineno=73,
                  end_col_offset=33),
                lineno=73,
                col_offset=8,
                end_lineno=73,
                end_col_offset=33),
              keyword(
                arg='import_to_file_map',
                value=Name(
                  id='import_to_file_map',
                  ctx=Load(),
                  lineno=73,
                  col_offset=54,
                  end_lineno=73,
                  end_col_offset=72),
                lineno=73,
                col_offset=35,
                end_lineno=73,
                end_col_offset=72)],
            lineno=72,
            col_offset=23,
            end_lineno=74,
            end_col_offset=5),
          lineno=72,
          col_offset=4,
          end_lineno=74,
          end_col_offset=5),
        Return(
          value=Name(
            id='all_imports_list',
            ctx=Load(),
            lineno=76,
            col_offset=11,
            end_lineno=76,
            end_col_offset=27),
          lineno=76,
          col_offset=4,
          end_lineno=76,
          end_col_offset=27)],
      decorator_list=[],
      lineno=62,
      col_offset=0,
      end_lineno=76,
      end_col_offset=27)],
  type_ignores=[])
```
</details>

