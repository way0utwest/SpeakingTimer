using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpeakerTimerWin
{
    class SpeakerTimer
    {
        //public alarms list<>TimeSpan;
        public TimeSpan sessionLength;

        public void SpeakerWimerWin()
        {
            // Load defaults
            sessionLength = TimeSpan.FromMinutes(5);
        }

    }
}
