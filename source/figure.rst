=============================================
いろいろな図
=============================================

blockdiagエクステンションを使うとUMLライクな図を描くことができます。

1. ブロック図
=================================

.. blockdiag::

.. blockdiag::
  :desctable:
  
  blockdiag {
     A -> B -> C;
     A [description = "browsers in each client"];
     B [description = "web server"];
     C [description = "database server"];
  }

2. シーケンス図
=================================

.. seqdiag::
  :desctable:

  seqdiag {
     A -> B -> C;
     A [description = "browsers in each client"];
     B [description = "web server"];
     C [description = "database server"];
  }

3. アクティビティ図
=================================

.. actdiag::

  actdiag {
      write -> convert -> image
      lane user {
          label = "User"
          write [label = "Writing reST"];
          image [label = "Get diagram IMAGE"];
      }
      lane actdiag {
          convert [label = "Convert reST to Image"];
      }
  }

4. ネットワーク図
=================================

.. nwdiag::
  :desctable:

  nwdiag {
     network {
       A [address = 192.168.0.1, description = "web server01"];
       B [address = 192.168.0.2, description = "web server02"];
     }
     network {
       A [address = 172.0.0.1];
       C [address = 172.0.0.2, description = "database server"];
     }
  }