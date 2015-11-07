#part1

class NewsStory(object):
  
  def __init__(self, guid, title, subject, summary, link):
    self.guid = guid
    self.title = title
    self.subject = subject
    self.summary = summary
    self.link = link

  def getGuid(self):
    return self.guid

  def getTitle(self):
    return self.title

  def getSubject(self):
    return self.subject

  def getSummary(self):
    return self.summary

  def getLink(self):
    return self.link
#txt = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')

#part 2-- triggers

class Trigger(object):
    def evaluate(self, story):
        """
	Returns True if an alert should be generated
	for the given news item, or False otherwise.
	"""
	raise NotImplementedError

# Enter your code for WordTrigger, TitleTrigger, 
# SubjectTrigger, and SummaryTrigger in this box
class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word
        
    def isWordIn(self, text):
        text = [a.strip(string.punctuation).lower() for a in text.split(" ")]
        for word in text:
            if self.word.lower() in word.split("'"):
                return True
        return False
        

class TitleTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        

class SubjectTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSubject())


class SummaryTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

# Composit triggers

class NotTrigger(Trigger):

    def __init__(self, t1):
        self.t1 = t1

    def evaluate(self, story):
        return not self.t1.evaluate(story)


class AndTrigger(Trigger):

    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)

        
class OrTrigger(Trigger):

    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)

# phrase Trigger

class PhraseTrigger(Trigger):

    def __init__(self, phrase):
        self.phrase = phrase

    def isPhraseIn(self,text):
        return self.phrase in text

    def evaluate(self, story):
        if self.isPhraseIn(story.getTitle()):
            return True
        if self.isPhraseIn(story.getSummary()):
            return True
        if self.isPhraseIn(story.getSubject()):
            return True

# filtering

def filterStories(stories, triggerlist):
    output = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                output.append(story)
                break
    return output

# make trigger

# Enter your code for makeTrigger in this box
#the questtion is not completely answered

