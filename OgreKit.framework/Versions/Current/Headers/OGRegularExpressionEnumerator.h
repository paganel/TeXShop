/*
 * Name: OGRegularExpressionEnumerator.h
 * Project: OgreKit
 *
 * Creation Date: Sep 03 2003
 * Author: Isao Sonobe <sonobe@gauge.scphys.kyoto-u.ac.jp>
 * Copyright: Copyright (c) 2003 Isao Sonobe, All rights reserved.
 * License: OgreKit License
 *
 * Encoding: UTF8
 * Tabsize: 4
 */

#import <Foundation/Foundation.h>

@class OGRegularExpression;

// Exception
extern NSString	* const OgreEnumeratorException;

@interface OGRegularExpressionEnumerator : NSEnumerator <NSCopying, NSCoding>
{
	OGRegularExpression	*_regex;							// ���K�\���I�u�W�F�N�g
	NSString			*_swappedTargetString;				// �����Ώە�����B\������ւ���Ă���(��������)�̂Œ���
	unsigned char		*_utf8SwappedTargetString;			// UTF8�ł̌����Ώە�����
	unsigned			_utf8lengthOfSwappedTargetString;	// strlen([_swappedTargetString UTF8String])
	NSRange				_searchRange;						// �����͈�
	unsigned			_searchOptions;						// �����I�v�V����
	int					_utf8TerminalOfLastMatch;			// �O��Ƀ}�b�`����������̏I�[�ʒu  (_region->end[0])
	unsigned			_startLocation;						// �}�b�`�J�n�ʒu
	unsigned			_utf8StartLocation;					// UTF8�ł̃}�b�`�J�n�ʒu
	BOOL				_isLastMatchEmpty;					// �O��̃}�b�`���󕶎��񂾂������ǂ���
	
	unsigned			_numberOfMatches;					// �}�b�`������
}

// �S�}�b�`���ʂ�z��ŕԂ��B
- (NSArray*)allObjects;
// ���̃}�b�`���ʂ�Ԃ��B
- (id)nextObject;

// description
- (NSString*)description;

@end