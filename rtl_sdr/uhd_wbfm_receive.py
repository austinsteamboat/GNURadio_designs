#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: UHD WBFM Receive
# Author: Example
# Description: WBFM Receive
# Generated: Mon Dec  1 16:55:49 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import osmosdr
import sip
import sys

from distutils.version import StrictVersion
class uhd_wbfm_receive(gr.top_block, Qt.QWidget):

    def __init__(self, address="addr=192.168.10.2", samp_rate=400e3, gain=0, audio_output="", freq=97.3e6):
        gr.top_block.__init__(self, "UHD WBFM Receive")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("UHD WBFM Receive")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "uhd_wbfm_receive")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.address = address
        self.samp_rate = samp_rate
        self.gain = gain
        self.audio_output = audio_output
        self.freq = freq

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 1
        self.tun_gain = tun_gain = 10
        self.tun_freq = tun_freq = freq/1e6
        self.fine = fine = 0
        self.audio_decim = audio_decim = 10

        ##################################################
        # Blocks
        ##################################################
        self._volume_layout = Qt.QVBoxLayout()
        self._volume_tool_bar = Qt.QToolBar(self)
        self._volume_layout.addWidget(self._volume_tool_bar)
        self._volume_tool_bar.addWidget(Qt.QLabel("Volume"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._volume_counter = qwt_counter_pyslot()
        self._volume_counter.setRange(0, 10, 0.1)
        self._volume_counter.setNumButtons(2)
        self._volume_counter.setValue(self.volume)
        self._volume_tool_bar.addWidget(self._volume_counter)
        self._volume_counter.valueChanged.connect(self.set_volume)
        self._volume_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._volume_slider.setRange(0, 10, 0.1)
        self._volume_slider.setValue(self.volume)
        self._volume_slider.setMinimumWidth(200)
        self._volume_slider.valueChanged.connect(self.set_volume)
        self._volume_layout.addWidget(self._volume_slider)
        self.top_grid_layout.addLayout(self._volume_layout, 1, 0, 1, 4)
        self._tun_gain_layout = Qt.QVBoxLayout()
        self._tun_gain_tool_bar = Qt.QToolBar(self)
        self._tun_gain_layout.addWidget(self._tun_gain_tool_bar)
        self._tun_gain_tool_bar.addWidget(Qt.QLabel("UHD Gain"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._tun_gain_counter = qwt_counter_pyslot()
        self._tun_gain_counter.setRange(0, 20, 1)
        self._tun_gain_counter.setNumButtons(2)
        self._tun_gain_counter.setValue(self.tun_gain)
        self._tun_gain_tool_bar.addWidget(self._tun_gain_counter)
        self._tun_gain_counter.valueChanged.connect(self.set_tun_gain)
        self._tun_gain_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._tun_gain_slider.setRange(0, 20, 1)
        self._tun_gain_slider.setValue(self.tun_gain)
        self._tun_gain_slider.setMinimumWidth(200)
        self._tun_gain_slider.valueChanged.connect(self.set_tun_gain)
        self._tun_gain_layout.addWidget(self._tun_gain_slider)
        self.top_layout.addLayout(self._tun_gain_layout)
        self._tun_freq_layout = Qt.QVBoxLayout()
        self._tun_freq_tool_bar = Qt.QToolBar(self)
        self._tun_freq_layout.addWidget(self._tun_freq_tool_bar)
        self._tun_freq_tool_bar.addWidget(Qt.QLabel("UHD Freq (MHz)"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._tun_freq_counter = qwt_counter_pyslot()
        self._tun_freq_counter.setRange(10, 1700, 1)
        self._tun_freq_counter.setNumButtons(2)
        self._tun_freq_counter.setValue(self.tun_freq)
        self._tun_freq_tool_bar.addWidget(self._tun_freq_counter)
        self._tun_freq_counter.valueChanged.connect(self.set_tun_freq)
        self._tun_freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._tun_freq_slider.setRange(10, 1700, 1)
        self._tun_freq_slider.setValue(self.tun_freq)
        self._tun_freq_slider.setMinimumWidth(200)
        self._tun_freq_slider.valueChanged.connect(self.set_tun_freq)
        self._tun_freq_layout.addWidget(self._tun_freq_slider)
        self.top_grid_layout.addLayout(self._tun_freq_layout, 0,0,1,2)
        self._fine_layout = Qt.QVBoxLayout()
        self._fine_tool_bar = Qt.QToolBar(self)
        self._fine_layout.addWidget(self._fine_tool_bar)
        self._fine_tool_bar.addWidget(Qt.QLabel("Fine Freq (MHz)"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._fine_counter = qwt_counter_pyslot()
        self._fine_counter.setRange(-.1, .1, .01)
        self._fine_counter.setNumButtons(2)
        self._fine_counter.setValue(self.fine)
        self._fine_tool_bar.addWidget(self._fine_counter)
        self._fine_counter.valueChanged.connect(self.set_fine)
        self._fine_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._fine_slider.setRange(-.1, .1, .01)
        self._fine_slider.setValue(self.fine)
        self._fine_slider.setMinimumWidth(200)
        self._fine_slider.valueChanged.connect(self.set_fine)
        self._fine_layout.addWidget(self._fine_slider)
        self.top_grid_layout.addLayout(self._fine_layout, 0,2,1,2)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(2.4e6)
        self.rtlsdr_source_0.set_center_freq((tun_freq+fine)*1e6, 0)
        self.rtlsdr_source_0.set_freq_corr(65, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(tun_gain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	tun_freq, #fc
        	2.4e6, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 2.4e6, 115e3, 30e3, firdes.WIN_HANN, 6.76))
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/aanderson/Documents/KBCO_record.wav", 1, 96000, 8)
        self.blocks_multiply_const_vxx = blocks.multiply_const_vff((volume, ))
        self.audio_sink = audio.sink(96000, audio_output, True)
        self.analog_wfm_rcv = analog.wfm_rcv(
        	quad_rate=2.4e6,
        	audio_decimation=25,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv, 0))
        self.connect((self.analog_wfm_rcv, 0), (self.blocks_multiply_const_vxx, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx, 0), (self.audio_sink, 0))
        self.connect((self.blocks_multiply_const_vxx, 0), (self.blocks_wavfile_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_wbfm_receive")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_audio_output(self):
        return self.audio_output

    def set_audio_output(self, audio_output):
        self.audio_output = audio_output

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_tun_freq(self.freq/1e6)

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        Qt.QMetaObject.invokeMethod(self._volume_counter, "setValue", Qt.Q_ARG("double", self.volume))
        Qt.QMetaObject.invokeMethod(self._volume_slider, "setValue", Qt.Q_ARG("double", self.volume))
        self.blocks_multiply_const_vxx.set_k((self.volume, ))

    def get_tun_gain(self):
        return self.tun_gain

    def set_tun_gain(self, tun_gain):
        self.tun_gain = tun_gain
        Qt.QMetaObject.invokeMethod(self._tun_gain_counter, "setValue", Qt.Q_ARG("double", self.tun_gain))
        Qt.QMetaObject.invokeMethod(self._tun_gain_slider, "setValue", Qt.Q_ARG("double", self.tun_gain))
        self.rtlsdr_source_0.set_gain(self.tun_gain, 0)

    def get_tun_freq(self):
        return self.tun_freq

    def set_tun_freq(self, tun_freq):
        self.tun_freq = tun_freq
        self.rtlsdr_source_0.set_center_freq((self.tun_freq+self.fine)*1e6, 0)
        Qt.QMetaObject.invokeMethod(self._tun_freq_counter, "setValue", Qt.Q_ARG("double", self.tun_freq))
        Qt.QMetaObject.invokeMethod(self._tun_freq_slider, "setValue", Qt.Q_ARG("double", self.tun_freq))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.tun_freq, 2.4e6)

    def get_fine(self):
        return self.fine

    def set_fine(self, fine):
        self.fine = fine
        Qt.QMetaObject.invokeMethod(self._fine_counter, "setValue", Qt.Q_ARG("double", self.fine))
        Qt.QMetaObject.invokeMethod(self._fine_slider, "setValue", Qt.Q_ARG("double", self.fine))
        self.rtlsdr_source_0.set_center_freq((self.tun_freq+self.fine)*1e6, 0)

    def get_audio_decim(self):
        return self.audio_decim

    def set_audio_decim(self, audio_decim):
        self.audio_decim = audio_decim

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
    parser.add_option("-a", "--address", dest="address", type="string", default="addr=192.168.10.2",
        help="Set IP Address [default=%default]")
    parser.add_option("-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(400e3),
        help="Set Sample Rate [default=%default]")
    parser.add_option("-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Default Gain [default=%default]")
    parser.add_option("-O", "--audio-output", dest="audio_output", type="string", default="",
        help="Set Audio Output Device [default=%default]")
    parser.add_option("-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(97.3e6),
        help="Set Default Frequency [default=%default]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = uhd_wbfm_receive(address=options.address, samp_rate=options.samp_rate, gain=options.gain, audio_output=options.audio_output, freq=options.freq)
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
