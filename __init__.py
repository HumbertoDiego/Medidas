# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Medidas
                                 A QGIS plugin
 Este Plugin mede o comprimento para todas as feicoes do tipo linha, bem como mede o perimetro e area para feicoes do tipo poligono.
                             -------------------
        begin                : 2017-04-15
        copyright            : (C) 2017 by Leandro Franca
        email                : franca.leandro@eb.mil.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Medidas class from file Medidas.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .medidas import Medidas
    return Medidas(iface)
