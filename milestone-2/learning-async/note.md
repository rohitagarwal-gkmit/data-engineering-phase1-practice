```notepad
┌─────────────────────────────────────────────────────────────────────────┐
│                        DECISION MATRIX                                  │
├─────────────────┬───────────────┬──────────────┬─────────────────────────┤
│  Task Type      │  Best Choice  │  Threads/    │  Internal Mechanism     │
│                 │               │  Processes   │                         │
├─────────────────┼───────────────┼──────────────┼─────────────────────────┤
│ I/O Bound       │ ASYNC/AWAIT   │ None         │ Event loop, single      │
│ (Network, DB,   │               │              │ thread, context         │
│  File)          │               │              │ switching               │
├─────────────────┼───────────────┼──────────────┼─────────────────────────┤
│ I/O Bound       │ THREADING     │ Threads      │ OS-level threads,       │
│ (When async     │               │ created      │ GIL released on I/O,    │
│  not available) │               │              │ context switching       │
├─────────────────┼───────────────┼──────────────┼─────────────────────────┤
│ CPU Bound       │ MULTIPROCESS  │ Processes    │ Separate Python         │
│ (Calculations,  │               │ created      │ interpreters, separate  │
│  Data process)  │               │              │ memory, true parallel   │
├─────────────────┼───────────────┼──────────────┼─────────────────────────┤
│ Mixed           │ ASYNC +       │ None +       │ Event loop + process    │
│ (I/O + CPU)     │ MULTIPROCESS  │ Processes    │ pool                    │
└─────────────────┴───────────────┴──────────────┴─────────────────────────┘

ASYNC/AWAIT Internal:
┌──────────────────────────────────────────────────────────────┐
│  Main Thread                                                 │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  Event Loop                                            │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐             │  │
│  │  │ Coroutine│  │ Coroutine│  │ Coroutine│             │  │
│  │  │    1     │  │    2     │  │    3     │             │  │
│  │  └──────────┘  └──────────┘  └──────────┘             │  │
│  │       ↓             ↓             ↓                    │  │
│  │    await         await         await                  │  │
│  │       ↓             ↓             ↓                    │  │
│  │  (suspended)   (suspended)   (running)                │  │
│  └────────────────────────────────────────────────────────┘  │
│  NO new threads/processes created!                           │
└──────────────────────────────────────────────────────────────┘

THREADING Internal:
┌──────────────────────────────────────────────────────────────┐
│  Process (PID: 12345)                                        │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │  Thread 1  │  │  Thread 2  │  │  Thread 3  │             │
│  │  (TID:100) │  │  (TID:101) │  │  (TID:102) │             │
│  │            │  │            │  │            │             │
│  │  Shared    │  │  Shared    │  │  Shared    │             │
│  │  Memory    │  │  Memory    │  │  Memory    │             │
│  └────────────┘  └────────────┘  └────────────┘             │
│         ↓              ↓              ↓                      │
│      GIL: Only one thread executes Python bytecode at once  │
│      I/O operations release GIL                             │
└──────────────────────────────────────────────────────────────┘

MULTIPROCESSING Internal:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Process 1      │  │  Process 2      │  │  Process 3      │
│  PID: 12345     │  │  PID: 12346     │  │  PID: 12347     │
│  ┌───────────┐  │  │  ┌───────────┐  │  │  ┌───────────┐  │
│  │  Memory   │  │  │  │  Memory   │  │  │  │  Memory   │  │
│  │  Space    │  │  │  │  Space    │  │  │  │  Space    │  │
│  │  (Isolated)│ │  │  │  (Isolated)│ │  │  │  (Isolated)│ │
│  └───────────┘  │  │  └───────────┘  │  │  └───────────┘  │
│  Own GIL        │  │  Own GIL        │  │  Own GIL        │
└─────────────────┘  └─────────────────┘  └─────────────────┘
        │                    │                    │
        └────────────────────┴────────────────────┘
                   True Parallelism
                   Different CPU cores
```
