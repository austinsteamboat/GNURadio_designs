#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Nov 20 18:10:21 2014
##################################################

from baz import acars_printer
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import baz
import osmosdr
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Message Queues
        ##################################################
        baz_acars_decoder_0_msgq_out = baz_acars_printer_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(2.4e6)
        self.rtlsdr_source_0.set_center_freq(1090e6, 0)
        self.rtlsdr_source_0.set_freq_corr(65, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(50, 0)
        self.rtlsdr_source_0.set_if_gain(10, 0)
        self.rtlsdr_source_0.set_bb_gain(10, 0)
        self.rtlsdr_source_0.set_antenna("RX", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.baz_acars_printer_0 = acars_printer.queue_watcher_thread(baz_acars_printer_0_msgq_in)
        self.baz_acars_decoder_0 = baz.acars_decoder(baz_acars_decoder_0_msgq_out)
        self.baz_acars_decoder_0.set_preamble_threshold(-1)
        self.baz_acars_decoder_0.set_frequency(0.0)
        self.baz_acars_decoder_0.set_station_name("")

        ##################################################
        # Connections
        ##################################################
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.baz_acars_decoder_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.baz_acars_decoder_0, 1))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
