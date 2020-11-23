import psutil
def test_cpu_freq(self):
        def check_ls(ls):
            for nt in ls:
                self.assertEqual(nt._fields, ('current', 'min', 'max'))
                self.assertLessEqual(nt.current, nt.max)
                for name in nt._fields:
                    value = getattr(nt, name)
                    self.assertIsInstance(value, (int, long, float))
                    self.assertGreaterEqual(value, 0)

        ls = psutil.cpu_freq(percpu=True)
        if TRAVIS and not ls:
            return

        assert ls, ls
        check_ls([psutil.cpu_freq(percpu=False)])

        if LINUX:
            self.assertEqual(len(ls), psutil.cpu_count()) 
test_cpu_freq()