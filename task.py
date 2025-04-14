from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
import json
import uuid


class Status(Enum):
    TODO = "todo"
    DONE = "done"


drafts: list[TaskDraft]=[]
tasks: list[Task] = []

def print_list(list: list[State]):
    for t in list:
        print(t.__dict__)


class TaskContext:
    def __init__(self, state: State):
        self._state: State = state
        self._state.context = self

    def transition_to(self, state: State):
        print(f"[Context] Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    @property
    def state(self) -> State:
        return self._state


    def publish(self):
        if isinstance(self._state, SupportsPublish):
            self._state.publish()
        else:
            raise RuntimeError(f"Publish not supported in state: {type(self._state).__name__}")

    def save(self):
        if isinstance(self._state, SupportsSave):
            self._state.save()
        else:
            raise RuntimeError(f"Save not supported in state: {type(self._state).__name__}")

    def complete(self):
        if isinstance(self._state, SupportsComplete):
            self._state.complete()
        else:
            raise RuntimeError(f"Complete not supported in state: {type(self._state).__name__}")


class State(ABC):
    _context: TaskContext
    _id: str
    _title: str
    _description: str

    def __init__(self, title: str, description: str):
        self._title = title
        self._description = description
        self._id = str(uuid.uuid4())

    @property
    def context(self) -> TaskContext:
        return self._context

    @context.setter
    def context(self, ctx: TaskContext):
        self._context = ctx

    @property
    def id(self) -> str:
        return self._id
    
    @context.setter
    def id(self, id: str):
        self._id = id

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description
    
    def to_str(self):
        json.dumps(self)


class SupportsPublish(ABC):
    @abstractmethod
    def publish(self) -> None: ...


class SupportsSave(ABC):
    @abstractmethod
    def save(self) -> None: ...


class SupportsComplete(ABC):
    @abstractmethod
    def complete(self) -> None: ...


class TaskDraft(State, SupportsPublish, SupportsSave):
    
    @State.title.setter
    def title(self, value: str):
        print(f"[Draft] Title updated: {value}")
        self._title = value

    @State.description.setter
    def description(self, value: str):
        print(f"[Draft] Description updated: {value}")
        self._description = value

    def save(self) -> None:
        print(f"[Draft] Saving draft: '{self.title}'")
        for i, o in enumerate(drafts):
            if o.id == self.id:
                drafts[i] = self
                break

    def publish(self) -> None:
        global drafts
        print("[Draft] Publishing draft...")
        self.context.transition_to(Task(self.title, self.description))
        filtered = filter(lambda dt: dt.id != self.id, drafts)
        drafts = list(filtered)

class Task(State, SupportsComplete):
    id: str
    status: Status

    def __init__(self, title: str, description: str):
        super().__init__(title, description)
        self.id = id
        self.status = Status.TODO
        tasks.append(self)
       

    def complete(self) -> None:
        print(f"[Task] Completing task '{self.title}'...")
        self.status = Status.DONE
        print(f"[Task] Task '{self.title}' is now DONE.")

